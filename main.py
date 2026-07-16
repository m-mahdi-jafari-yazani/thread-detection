import numpy as np
import matplotlib.pyplot as plt

from src.image_utils import load_image
from src.filters import (
    generate_filter_bank,
    apply_filter
)

image = load_image(
    "data/non_threaded/image1.jpg",
    scale=0.5
)

filters = generate_filter_bank()

scores = []

for kernel in filters:

    response = apply_filter(image, kernel)

    score = np.mean(np.abs(response))

    scores.append(score)

best_score = max(scores)

print(f"Best Response = {best_score:.2f}")

plt.bar(range(len(scores)), scores)
plt.title("Filter Responses")
plt.xlabel("Filter Index")
plt.ylabel("Response")
plt.show()