import json
from typing import Dict, Any
from .benchmark_loader import BenchmarkLoader
from .scaledown_client import ScaleDownClient
from .gemini_client import GeminiClient
from .exceptions import AIModelComparisonError

class ComparisonPipeline:
    def __init__(self):
        self.loader = BenchmarkLoader()
        self.scaledown = ScaleDownClient()
        self.gemini = GeminiClient()

    def run(self, problem_description: str) -> Dict[str, Any]:
        """Runs the comparison pipeline end-to-end."""
        try:
            # 1. Load benchmarks
            benchmarks = self.loader.load()
            
            # 2. Optimize prompt via ScaleDown.ai
            # Use benchmarks as context for optimization
            context = json.dumps(benchmarks)
            optimized_prompt = self.scaledown.optimize_prompt(problem_description, context)
            
            # 3. Analyze and Rank via Gemini
            results = self.gemini.analyze_and_rank(optimized_prompt, benchmarks)
            
            return {
                "problem": problem_description,
                "optimized_prompt": optimized_prompt,
                "analysis": results,
                "status": "success"
            }
        except AIModelComparisonError as e:
            return {
                "error": str(e),
                "status": "error"
            }
        except Exception as e:
            return {
                "error": f"Unexpected pipeline failure: {e}",
                "status": "error"
            }
