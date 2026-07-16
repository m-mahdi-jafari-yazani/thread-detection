import matplotlib.pyplot as plt

from src.image_utils import load_image


image = load_image(
    "data/threaded/image1.jpg",
    scale=0.5
)

plt.imshow(image, cmap="gray")
plt.title("Threaded Screw")
plt.axis("off")
plt.show()