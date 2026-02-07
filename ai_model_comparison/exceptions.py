class AIModelComparisonError(Exception):
    """Base exception for the tool."""
    pass

class ScaleDownError(AIModelComparisonError):
    """Raised when ScaleDown API fails."""
    pass

class GeminiError(AIModelComparisonError):
    """Raised when Gemini API fails."""
    pass

class BenchmarkError(AIModelComparisonError):
    """Raised when benchmark data cannot be loaded."""
    pass
