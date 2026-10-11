import numpy as np
import re

print("=== Повторение Дней 17–18 ===")

# Косинусное сходство (День 17)
def cosine_similarity(a, b):
    dot = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)

a = np.array([1, 2, 3])
b = np.array([2, 4, 6])
print(f"cos_sim([1,2,3], [2,4,6]) = {cosine_similarity(a, b):.4f}")
print("(Должно быть 1.0 — одно направление)")

# Нормы (День 17)
v = np.array([3, -4, 12])
print(f"\nL1-норма: {np.linalg.norm(v, 1)}")
print(f"L2-норма: {np.linalg.norm(v):.4f}")
print(f"L∞-норма: {np.linalg.norm(v, np.inf)}")

# Матричные операции (День 14)
X = np.array([
    [25, 175, 70],
    [30, 165, 55],
    [35, 180, 85],
])
print(f"\nМатрица признаков:")
print(X)
print(f"X.T @ X:")
print(X.T @ X)

# TF-IDF концепция (День 18)
print("\n=== TF-IDF концепция ===")
docs = ["кошка сидит", "собака сидит", "кошка и собака"]
vocab = sorted(set(w for d in docs for w in d.lower().split()))
print(f"Словарь: {vocab}")
print("TF-IDF = TF × IDF")
print("  TF — частота слова в документе")
print("  IDF — редкость слова в коллекции")

