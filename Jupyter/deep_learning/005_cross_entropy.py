import numpy as np


def cross_entropy(Y, P):
    """
    Y = [1,1,0]
    P = [0.8, 0.7, 0.9]
    """
    y_float = np.float_(Y)
    p_float = np.float_(P)
    entropy = y_float*np.log(p_float)+(1-y_float)*np.log(1-p_float)
    return np.sum(-entropy)
