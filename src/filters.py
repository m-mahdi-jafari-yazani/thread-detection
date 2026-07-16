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



def generate_filter_bank(size=31):
    """
    Generate cosine filters with different
    frequencies and orientations.
    """

    filters = []

    frequencies = [0.2, 0.4, 0.6]

    angles = [
        0,
        np.pi / 6,
        np.pi / 3,
        np.pi / 2,
        2 * np.pi / 3,
        5 * np.pi / 6
    ]

    for freq in frequencies:

        for angle in angles:

            a = freq * np.cos(angle)
            b = freq * np.sin(angle)

            kernel = cosine_filter(size, a, b)

            filters.append(kernel)

    return filters