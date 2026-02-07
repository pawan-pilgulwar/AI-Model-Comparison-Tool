import unittest
from unittest.mock import MagicMock, patch
from ai_model_comparison.pipeline import ComparisonPipeline

class TestPipeline(unittest.TestCase):
    def setUp(self):
        self.pipeline = ComparisonPipeline()

    @patch('ai_model_comparison.scaledown_client.ScaleDownClient.optimize_prompt')
    @patch('ai_model_comparison.gemini_client.GeminiClient.analyze_and_rank')
    def test_pipeline_success(self, mock_gemini, mock_scaledown):
        # Mocking external calls
        mock_scaledown.return_value = "optimized prompt"
        mock_gemini.return_value = {
            "task_type": "Classification",
            "rankings": [{"model": "GPT-4", "rank": 1, "reason": "Good"}],
            "trade_offs": "Cost vs Speed"
        }

        result = self.pipeline.run("Some problem")
        
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["optimized_prompt"], "optimized prompt")
        self.assertEqual(result["analysis"]["task_type"], "Classification")

if __name__ == "__main__":
    unittest.main()
