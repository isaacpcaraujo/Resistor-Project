from pydantic import BaseModel, Field
from typing import Dict, Any

class ModelConfig(BaseModel):
    type: str = Field(..., description="Model type, e.g., 'cnn-1d', 'xgboost'")
    hyperparameters: Dict[str, Any] = Field(default_factory=dict)
