from pydantic import BaseModel
from .dataset_config import DatasetConfig
from .model_config import ModelConfig
from .training_config import TrainingConfig
from .evaluation_config import EvaluationConfig

class PreprocessingConfig(BaseModel):
    normalize: bool = True
    remove_outliers: bool = False
    feature_selection: bool = False

class ExperimentConfig(BaseModel):
    experiment_name: str
    dataset: DatasetConfig
    preprocessing: PreprocessingConfig = PreprocessingConfig()
    model: ModelConfig
    training: TrainingConfig = TrainingConfig()
    evaluation: EvaluationConfig = EvaluationConfig()
