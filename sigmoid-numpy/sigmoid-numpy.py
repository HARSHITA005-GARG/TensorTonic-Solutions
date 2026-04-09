import numpy as np
import math

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    n = np.array(x)
    s = 1/ (1 + np.exp(-n))
    return s