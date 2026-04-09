import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    # Write code here
    n = np.array(x)
    return np.where(n >=0, n, alpha*n)
    