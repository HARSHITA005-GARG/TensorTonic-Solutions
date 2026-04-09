import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    # Write code here
    return np.where(np.array(x) > 0, np.array(x), 0)