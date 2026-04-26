import tensorflow as tf
from tensorflow.keras import layers, models

def build_cnn_1d(input_shape, filters=[16, 32], kernel_size=3, dropout_rate=0.2):
    """
    Factory function to build a 1D CNN for ring data.
    """
    model = models.Sequential()
    model.add(layers.InputLayer(input_shape=input_shape))
    model.add(layers.Reshape((input_shape[0], 1)))
    
    for i, f in enumerate(filters):
        model.add(layers.Conv1D(filters=f, kernel_size=kernel_size, activation='relu', padding='same'))
        # You can add MaxPooling1D or BatchNormalization here
        
    model.add(layers.Flatten())
    model.add(layers.Dense(64, activation='relu'))
    if dropout_rate > 0:
        model.add(layers.Dropout(dropout_rate))
    model.add(layers.Dense(1, activation='sigmoid'))
    
    return model

def build_model(config):
    """
    Builds model based on config dictionary.
    """
    model_cfg = config.get("model", {})
    arch = model_cfg.get("architecture", "cnn_1d")
    
    rings = config.get("data", {}).get("rings", 100)
    input_shape = (rings,)
    
    if arch == "cnn_1d":
        return build_cnn_1d(
            input_shape=input_shape,
            filters=model_cfg.get("filters", [16, 32]),
            kernel_size=model_cfg.get("kernel_size", 3),
            dropout_rate=model_cfg.get("dropout", 0.2)
        )
    else:
        raise ValueError(f"Unknown architecture: {arch}")
