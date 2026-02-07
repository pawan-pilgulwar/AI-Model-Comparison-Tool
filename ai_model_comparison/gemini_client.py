import google.generativeai as genai
import json
import os
from typing import Dict, List, Any
from .config import config
from .exceptions import GeminiError

class GeminiClient:
    def __init__(self):
        self.api_key = config.GEMINI_API_KEY
        self.model_name = config.GEMINI_MODEL_NAME
        
        if self.api_key:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel(self.model_name)
        else:
            self.model = None
            print("Warning: Gemini API key not found in config.")

    def analyze_and_rank(self, optimized_prompt: str, benchmark_data: List[Dict]) -> Dict[str, Any]:
        """
        Uses Gemini to identify task type and rank models based on benchmarks.
        Returns a structured dictionary of results and reasoning.
        """
        if not self.model:
            raise GeminiError("Gemini client not initialized (missing API key).")

        benchmark_str = json.dumps(benchmark_data, indent=2)
        system_instruction = (
            "You are a senior AI research architect. Analyze the user's requirements "
            "and recommend models from the benchmark data below.\n\n"
            "Requirements for your response:\n"
            "- Rank models logically based on Accuracy (MMLU), Cost, and Latency trade-offs.\n"
            "- Identify the task type (e.g., Sentiment Analysis, RAG, Edge Inferences).\n"
            "- Provide human-readable explanations for why the top model was chosen and why others were ranked lower.\n"
            "- Format output STRICTLY as a JSON object.\n\n"
            "Benchmark Data:\n"
            f"{benchmark_str}\n\n"
            "JSON Format Example:\n"
            "{\n"
            "  'task_type': '...', \n"
            "  'rankings': [{'model': '...', 'rank': 1, 'reason': '...'}, ...],\n"
            "  'trade_offs': '...', \n"
            "  'final_summary': '...'\n"
            "}"
        )

        prompt = f"{system_instruction}\n\nOptimized Prompt:\n{optimized_prompt}"

        try:
            response = self.model.generate_content(
                prompt,
                generation_config=genai.GenerationConfig(
                    response_mime_type="application/json",
                )
            )
            
            content = response.text.strip()
            # Clean markdown JSON blocks
            if content.startswith("```json"):
                content = content.replace("```json", "", 1).replace("```", "", 1).strip()
            elif content.startswith("```"):
                content = content.replace("```", "", 1).replace("```", "", 1).strip()
            
            return json.loads(content)
        except Exception as e:
            raise GeminiError(f"Gemini generation failed: {e}")
