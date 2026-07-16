import glob

import cv2
import numpy as np
import os

from src.predictor import predictor


def add_gaussian_noise(image, variance):
    """
    Add Gaussian noise to an image.
    """

    image = image.astype(np.float32) / 255.0

    noise = np.random.normal(
        0,
        np.sqrt(variance),
        image.shape
    )

    noisy = image + noise

    noisy = np.clip(noisy, 0, 1)

    noisy = (255 * noisy).astype(np.uint8)

    return noisy


def load_dataset():

    images = []

    for path in sorted(glob.glob("data/threaded/*.jpg")):
        images.append((path, 1))

    for path in sorted(glob.glob("data/non_threaded/*.jpg")):
        images.append((path, 0))

    return images



def evaluate_noise(variance):

    dataset = load_dataset()

    correct = 0

    for path, label in dataset:

        image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

        noisy = add_gaussian_noise(
            image,
            variance
        )

        if variance == 0.05:
            cv2.imwrite("noisy_sample.jpg", noisy)

        temp = "temp.jpg"

        cv2.imwrite(temp, noisy)

        prediction, _ = predictor(temp)

        if prediction == label:
            correct += 1

    accuracy = correct / len(dataset)

    if os.path.exists("temp.jpg"):
        os.remove("temp.jpg")

    return accuracy