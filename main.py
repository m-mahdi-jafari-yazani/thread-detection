import matplotlib.pyplot as plt

from src.fft_detector import fft_from_image


threaded_image, threaded_fft = fft_from_image(
    "data/threaded/image1.jpg"
)

non_threaded_image, non_threaded_fft = fft_from_image(
    "data/non_threaded/image1.jpg"
)

plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.imshow(threaded_image, cmap="gray")
plt.title("Threaded")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(threaded_fft, cmap="gray")
plt.title("Threaded FFT")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(non_threaded_image, cmap="gray")
plt.title("Non-threaded")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(non_threaded_fft, cmap="gray")
plt.title("Non-threaded FFT")
plt.axis("off")

plt.tight_layout()
plt.show()