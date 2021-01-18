import numpy as np


def sigmoid(z):
    """
    :param z: scalar or any array
    :return: sigmoid of z
    """
    return 1 / (1 + np.exp(-z))
