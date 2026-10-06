import numpy as np

print("=== Повторение Дня 14 ===")

# Матрица признаков: строки — объекты, столбцы — признаки
X = np.array([
    [25, 175, 70],
    [30, 165, 55],
    [35, 180, 85],
    [28, 170, 60],
])

print("Матрица признаков:")
print(X)
print("Форма:", X.shape)

# Транспонирование
print("\nТранспонированная:")
print(X.T)
print("Форма:", X.T.shape)

# Среднее по каждому признаку
print("\nСреднее по столбцам (axis=0):")
print(np.mean(X, axis=0))

# Евклидово расстояние
def euclidean_distance(a, b):
    return np.sqrt(np.sum((a - b) ** 2))

print("\nЕвклидово расстояние между 1-м и 2-м объектом:")
print(euclidean_distance(X[0], X[1]))

print("\nВсё работает — идём дальше.")