import numpy as np
from scipy.signal import convolve2d


def cosine_filter(size, a, b):
    """
    Create a 2D cosine filter:
        cos(ax + by)
    """

    center = size // 2

    x = np.arange(-center, center + 1)
    y = np.arange(-center, center + 1)

    X, Y = np.meshgrid(x, y)

    kernel = np.cos(a * X + b * Y)

    return kernel

def apply_filter(image, kernel):
    """
    Apply 2D convolution between image and kernel.
    """

    response = convolve2d(
        image,
        kernel,
        mode="same",
        boundary="symm"
    )

    return response