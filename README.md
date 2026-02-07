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
