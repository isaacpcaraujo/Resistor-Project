from abc import ABC, abstractmethod
from typing import Any
from src.config.experiment_config import ExperimentConfig

class BaseModel(ABC):
    """Base class for all models."""
    def __init__(self, config: ExperimentConfig):
        self.config = config
        self.model = self._build_model()
        self._compile_model()
        
    @abstractmethod
    def _build_model(self) -> Any:
        """Builds the model architecture from configurations."""
        pass
        
    def _compile_model(self):
        """Compiles the model, if needed (e.g., TensorFlow). Optional for subclasses."""
        pass
        
    @abstractmethod
    def train(self, X_train, y_train, X_val=None, y_val=None):
        """Executes model training."""
        pass
        
    @abstractmethod
    def evaluate(self, X_test, y_test):
        """Evaluates and returns model metrics."""
        pass
