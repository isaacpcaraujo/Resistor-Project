from pydantic import BaseModel, Field

class DatasetConfig(BaseModel):
    path: str
    target_column: str = "label"
    train_split: float = Field(0.8, ge=0.1, le=0.99)
