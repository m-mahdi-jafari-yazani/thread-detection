import matplotlib.pyplot as plt

from src.image_utils import load_image
from src.filters import cosine_filter, apply_filter


image = load_image(
    "data/threaded/image1.jpg",
    scale=0.5
)

kernel = cosine_filter(
    size=31,
    a=0.5,
    b=0.3
)

response = apply_filter(image, kernel)

plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(image, cmap="gray")
plt.title("Input")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(kernel, cmap="gray")
plt.title("Cosine Filter")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(response, cmap="gray")
plt.title("Convolution")
plt.axis("off")

plt.tight_layout()
plt.show()