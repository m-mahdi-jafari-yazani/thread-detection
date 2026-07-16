import numpy as np

from src.fft_detector import fft_from_image, remove_low_frequencies


def predictor(path, threshold=12.6):
    """
    Return:
        1 -> Threaded
        0 -> Non-threaded
    """

    _, spectrum = fft_from_image(path)

    spectrum = remove_low_frequencies(
        spectrum,
        radius=20
    )

    values = np.sort(spectrum.ravel())

    score = np.mean(values[-10:])

    prediction = int(score > threshold)

    return prediction, score