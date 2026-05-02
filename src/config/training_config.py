from pydantic import BaseModel, Field

class TrainingConfig(BaseModel):
    random_seed: int = 42
    cross_validation_folds: int = Field(5, ge=2)
