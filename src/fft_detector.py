import numpy as np


def generate_cosine(size, fx, fy):
    """
    Generate a 2D cosine using integer frequency components.
    fx: horizontal frequency component
    fy: vertical frequency component
    """

    x = np.arange(size)
    y = np.arange(size)

    X, Y = np.meshgrid(x, y)

    image = np.cos(
        2 * np.pi * (fx * X + fy * Y) / size
    )

    return image


def compute_fft(image):
    """
    Compute centered 2D Fourier Transform.
    """

    fft = np.fft.fft2(image)

    fft_shifted = np.fft.fftshift(fft)

    magnitude = np.log1p(np.abs(fft_shifted))

    return magnitude