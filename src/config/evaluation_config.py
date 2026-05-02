from pydantic import BaseModel
from typing import List

class EvaluationConfig(BaseModel):
    metrics: List[str] = ["accuracy"]
