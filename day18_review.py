import numpy as np

print("=== Повторение Дня 17 ===")

# Косинусное сходство
def cosine_similarity(a, b):
    dot = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)

# Тест
a = np.array([1, 2, 3])
b = np.array([2, 4, 6])
c = np.array([0, 1, 0])

print(f"cos_sim(a, b) = {cosine_similarity(a, b):.4f}")  # 1.0 (одно направление)
print(f"cos_sim(a, c) = {cosine_similarity(a, c):.4f}")  # ~0.74

# Евклидово расстояние
def euclidean_distance(a, b):
    return np.linalg.norm(a - b)

print(f"\neuclidean(a, b) = {euclidean_distance(a, b):.4f}")
print(f"euclidean(a, c) = {euclidean_distance(a, c):.4f}")

print("\nКлючевое свойство косинуса:")
print("  Не зависит от длины вектора")
print("  Измеряет только направление")
print("  Идеален для сравнения текстов")

