import matplotlib.pyplot as plt
import numpy as np

from src.fft_detector import generate_cosine, compute_fft

image1 = generate_cosine(
    size=256,
    fx=8,
    fy=0
)

image2 = generate_cosine(
    size=256,
    fx=6,
    fy=6
)

fft1 = compute_fft(image1)
fft2 = compute_fft(image2)

plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.imshow(image1, cmap="gray")
plt.title("Cosine 1")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(fft1, cmap="gray")
plt.title("FFT 1")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(image2, cmap="gray")
plt.title("Cosine 2")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(fft2, cmap="gray")
plt.title("FFT 2")
plt.axis("off")

plt.tight_layout()
plt.show()