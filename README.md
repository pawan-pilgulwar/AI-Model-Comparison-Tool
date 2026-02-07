# AI Model Comparison Tool

A modular, research-oriented AI assistant that helps select models based on structured benchmarks.

## Features
- **Prompt Optimization**: Uses ScaleDown.ai REST API to compress and optimize contexts.
- **Intelligent Reasoning**: Uses Google Gemini to analyze constraints and rank models.
- **Premium UI**: Modern Flask-based web interface with glassmorphism design.

## Project Structure
- `ai_model_comparison/`: Core Python package.
- `templates/`: HTML components.
- `static/`: Design and styling.
- `tests/`: Automated test suite.
- `examples/`: Integration examples.

## Setup
1. `pip install -r requirements.txt`
2. Configure `.env` based on `.env.example`.
3. Run the app: `python -m ai_model_comparison.app`

## API Usage
Integration with ScaleDown.ai is done using standard HTTP REST calls (no SDK).
Gemini LLM handles all reasoning over benchmark data.


## Environment Variables
- `SCALEDOWN_API_KEY`: API key for ScaleDown.ai.
- `SCALEDOWN_API_URL`: API URL for ScaleDown.ai.
- `SCALEDOWN_PROJECT_ID`: Project ID for ScaleDown.ai.  
- `SCALEDOWN_MAX_TOKENS`: Maximum number of tokens for ScaleDown.ai.
- `GEMINI_API_KEY`: API key for Google Gemini.
- `GEMINI_MODEL_NAME`: Model name for Google Gemini.
- `FLASK_ENV=development`   : Set Flask environment to development.
- `FLASK_SECRET_KEY=generate_a_secure_key_here`: Set Flask secret key.