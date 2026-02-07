import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class Config:
    # Gemini
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    GEMINI_MODEL_NAME: str = os.getenv("GEMINI_MODEL_NAME", "gemini-flash-latest")
    
    # ScaleDown.ai
    SCALEDOWN_API_KEY: str = os.getenv("SCALEDOWN_API_KEY", "")
    SCALEDOWN_API_URL: str = os.getenv("SCALEDOWN_API_URL", "https://api.scaledown.xyz/v1/optimize")
    SCALEDOWN_PROJECT_ID: str = os.getenv("SCALEDOWN_PROJECT_ID", "ai-model-comparison")
    SCALEDOWN_MAX_TOKENS: int = int(os.getenv("SCALEDOWN_MAX_TOKENS", "1024"))
    
    # Flask
    FLASK_ENV: str = os.getenv("FLASK_ENV", "development")
    FLASK_SECRET_KEY: str = os.getenv("FLASK_SECRET_KEY", "dev-secret-key")
    PORT: int = int(os.getenv("PORT", "5000"))

config = Config()
