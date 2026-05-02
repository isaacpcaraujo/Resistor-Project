import json
from pathlib import Path
from .experiment_config import ExperimentConfig

def load_config(file_path: str) -> ExperimentConfig:
    """Loads, validates, and returns the experiment configuration from a JSON file."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Configuration file not found: {file_path}")
        
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    # Pydantic will automatically validate the data and raise ValidationError if there are issues
    return ExperimentConfig(**data)
