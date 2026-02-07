import json
import os
from typing import List, Dict
from .exceptions import BenchmarkError

class BenchmarkLoader:
    def __init__(self, file_path: str = None):
        if file_path is None:
            # Default to the data directory within the package
            file_path = os.path.join(os.path.dirname(__file__), 'data', 'benchmarks.json')
        self.file_path = file_path

    def load(self) -> List[Dict]:
        """Loads benchmark data from JSON."""
        if not os.path.exists(self.file_path):
            raise BenchmarkError(f"Benchmark file not found: {self.file_path}")
        
        try:
            with open(self.file_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            raise BenchmarkError(f"Failed to load benchmarks: {e}")
