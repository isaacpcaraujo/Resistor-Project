import numpy as np

def norm1(data):
    """
    Applies norm1 normalization across the rings.
    """
    norms = np.abs(data).sum(axis=1, keepdims=True)
    norms[norms == 0] = 1
    return data / norms

def fatiar_matriz_por_versao(data, version):
    """
    Slices the ring matrix based on the specified version.
    """
    if version == 0:
        return data  # Return all 100 rings
    elif version == 1:
        # Example slicing for version 1
        return data[:, 1:8]
    elif version == 2:
        # Example slicing for version 2
        return data[:, :25]
    else:
        raise ValueError(f"Unknown version: {version}")
        
def preprocess_data(x_data, config):
    """
    Applies full preprocessing pipeline.
    """
    version = config.get("version", 0)
    x_sliced = fatiar_matriz_por_versao(x_data, version)
    x_normed = norm1(x_sliced)
    return x_normed
