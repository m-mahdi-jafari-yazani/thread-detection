import cv2
import matplotlib.pyplot as plt

from src.noise_test import add_gaussian_noise

image = cv2.imread("data/threaded/image1.jpg", cv2.IMREAD_GRAYSCALE)

noisy = add_gaussian_noise(image, 0.05)

plt.subplot(1,2,1)
plt.imshow(image, cmap="gray")
plt.title("Original")

plt.subplot(1,2,2)
plt.imshow(noisy, cmap="gray")
plt.title("Noisy")

plt.show()