import cv2


def load_image(path, scale=0.5):
    """
    Load image, convert to grayscale and resize.
    """

    image = cv2.imread(path)

    if image is None:
        raise FileNotFoundError(f"Image not found: {path}")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    width = int(gray.shape[1] * scale)
    height = int(gray.shape[0] * scale)

    resized = cv2.resize(gray, (width, height))

    return resized

def crop_thread_region(image):
    """
    Keep only the central horizontal band where the threads are.
    """

    h, w = image.shape

    top = int(h * 0.30)
    bottom = int(h * 0.70)

    left = int(w * 0.10)
    right = int(w * 0.90)

    return image[top:bottom, left:right]