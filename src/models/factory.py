from src.config.experiment_config import ExperimentConfig
from src.models.base_model import BaseModel
from src.models.tensorflow.cnn1d import CNN1DModel

class ModelFactory:
    """Model factory (Factory Pattern) to dynamically handle multiple architectures."""
    
    _registry = {
        "cnn-1d": CNN1DModel,
        # Future:
        # "xgboost": XGBoostModel,
        # "mlp": MLPModel
    }
    
    @classmethod
    def register_model(cls, name: str, model_class: type):
        """Allows registering new models dynamically without altering if/else blocks."""
        cls._registry[name] = model_class
        
    @classmethod
    def create(cls, config: ExperimentConfig) -> BaseModel:
        """Instantiates the appropriate model based on the type string in the config."""
        model_type = config.model.type
        if model_type not in cls._registry:
            supported = list(cls._registry.keys())
            raise ValueError(f"Model '{model_type}' is not supported. Available models: {supported}")
            
        model_class = cls._registry[model_type]
        return model_class(config)
