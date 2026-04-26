import tensorflow as tf
import numpy as np

class SPCallback(tf.keras.callbacks.Callback):
    """
    Custom callback to calculate the SP (Soma-Produto) index at the end of each epoch.
    SP = sqrt(sqrt(PD * (1 - FA)) * (0.5 * (PD + (1 - FA))))
    """
    def __init__(self, validation_data):
        super(SPCallback, self).__init__()
        self.validation_data = validation_data
        
    def on_epoch_end(self, epoch, logs=None):
        val_x, val_y = self.validation_data
        val_predict = (self.model.predict(val_x, verbose=0) > 0.5).astype(int)
        
        # Reshape to 1D if needed
        val_y = np.reshape(val_y, -1)
        val_predict = np.reshape(val_predict, -1)
        
        tp = np.sum((val_predict == 1) & (val_y == 1))
        fn = np.sum((val_predict == 0) & (val_y == 1))
        fp = np.sum((val_predict == 1) & (val_y == 0))
        tn = np.sum((val_predict == 0) & (val_y == 0))
        
        pd = tp / (tp + fn) if (tp + fn) > 0 else 0.0 # Probability of Detection
        fa = fp / (fp + tn) if (fp + tn) > 0 else 0.0 # False Alarm rate
        
        sp = np.sqrt(np.sqrt(pd * (1 - fa)) * (0.5 * (pd + (1 - fa))))
        
        logs['val_sp'] = sp
