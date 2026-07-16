import os

import matplotlib.pyplot as plt

from src.fft_detector import (
    generate_cosine,
    compute_fft,
    fft_from_image,
)

from src.noise_test import evaluate_noise


os.makedirs("outputs", exist_ok=True)


def part1():

    image = generate_cosine(
        size=256,
        fx=8,
        fy=0
    )

    fft = compute_fft(image)

    plt.figure(figsize=(10,4))

    plt.subplot(1,2,1)
    plt.imshow(image, cmap="gray")
    plt.title("Cosine")

    plt.subplot(1,2,2)
    plt.imshow(fft, cmap="gray")
    plt.title("FFT")

    plt.tight_layout()

    plt.savefig(
        "outputs/cosine_fft.png",
        dpi=300
    )

    plt.show()


def part2():

    image, fft = fft_from_image(
        "data/threaded/image1.jpg"
    )

    plt.figure(figsize=(10,4))

    plt.subplot(1,2,1)
    plt.imshow(image, cmap="gray")
    plt.title("Threaded")

    plt.subplot(1,2,2)
    plt.imshow(fft, cmap="gray")
    plt.title("FFT")

    plt.tight_layout()

    plt.savefig(
        "outputs/thread_fft.png",
        dpi=300
    )

    plt.show()


def part3():

    variances = [
        0,
        0.001,
        0.003,
        0.005,
        0.01,
        0.02,
        0.05,
    ]

    accuracies = []

    for variance in variances:

        accuracy = evaluate_noise(
            variance
        )

        accuracies.append(accuracy)

        print(
            f"Variance={variance:.3f}"
            f" Accuracy={accuracy:.2f}"
        )

    plt.figure(figsize=(7,5))

    plt.plot(
        variances,
        accuracies,
        marker="o"
    )

    plt.xlabel("Noise Variance")
    plt.ylabel("Accuracy")
    plt.grid(True)

    plt.savefig(
        "outputs/noise_accuracy.png",
        dpi=300
    )

    plt.show()


def main():

    print("Part 1")
    part1()

    print("Part 2")
    part2()

    print("Part 3")
    part3()


if __name__ == "__main__":
    main()