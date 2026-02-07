import requests
from typing import Optional
from .config import config
from .exceptions import ScaleDownError

class ScaleDownClient:
    def __init__(self):
        self.api_key = config.SCALEDOWN_API_KEY
        self.api_url = config.SCALEDOWN_API_URL
        self.project_id = config.SCALEDOWN_PROJECT_ID
        self.max_tokens = config.SCALEDOWN_MAX_TOKENS

    def optimize_prompt(self, prompt: str, context: str) -> str:
        """
        Sends user prompt and benchmark context to ScaleDown.ai REST API.
        Enforces token limits and handles errors gracefully with fallbacks.
        """
        if not self.api_key or not self.api_url:
            print("Warning: ScaleDown.ai API keys not provided. Falling back to original prompt.")
            return prompt

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "prompt": prompt,
            "context": context,
            "project_id": self.project_id,
            "max_tokens": self.max_tokens
        }

        try:
            response = requests.post(self.api_url, json=payload, headers=headers, timeout=20)
            response.raise_for_status()
            data = response.json()
            return data.get("optimized_prompt", prompt)
        except Exception as e:
            print(f"ScaleDown error: {e}. Using original prompt as fallback.")
            # We don't raise here to maintain pipeline flow, but we log the warning.
            return prompt
