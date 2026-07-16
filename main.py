import matplotlib.pyplot as plt

from src.filters import cosine_filter


kernel = cosine_filter(
    size=31,
    a=0.5,
    b=0.3
)

plt.imshow(kernel, cmap="gray")
plt.title("Cosine Filter")
plt.colorbar()
plt.show()