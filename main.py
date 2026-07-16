import glob

from src.predictor import predictor

correct = 0
total = 0

print("Threaded")
for path in sorted(glob.glob("data/threaded/*.jpg")):

    pred, score = predictor(path)

    print(path, pred, f"{score:.2f}")

    correct += (pred == 1)
    total += 1

print()

print("Non-threaded")
for path in sorted(glob.glob("data/non_threaded/*.jpg")):

    pred, score = predictor(path)

    print(path, pred, f"{score:.2f}")

    correct += (pred == 0)
    total += 1

print()
print(f"Accuracy = {100 * correct / total:.1f}%")