import numpy as np

# === Создание 2D массивов ===

# Из вложенных списков
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
])

print("Матрица:")
print(matrix)
print("Тип:", type(matrix))
print("Форма (shape):", matrix.shape)
print("Размерность (ndim):", matrix.ndim)
print("Количество элементов (size):", matrix.size)
print("Тип данных (dtype):", matrix.dtype)

# === Специальные 2D массивы ===

# Матрица нулей
zeros = np.zeros((3, 4))
print("\nНули (3x4):")
print(zeros)

# Матрица единиц
ones = np.ones((2, 3))
print("\nЕдиницы (2x3):")
print(ones)

# Единичная матрица (диагональ из единиц)
identity = np.eye(4)
print("\nЕдиничная матрица (4x4):")
print(identity)

# Диагональная матрица
diagonal = np.diag([1, 2, 3, 4])
print("\nДиагональная матрица:")
print(diagonal)

# Матрица случайных чисел
random_matrix = np.random.random((3, 3))
print("\nСлучайная матрица (3x3):")
print(random_matrix)

# Матрица случайных целых чисел
random_int_matrix = np.random.randint(1, 100, size=(3, 4))
print("\nСлучайная целочисленная матрица (3x4):")
print(random_int_matrix)

# Матрица из arange + reshape
range_matrix = np.arange(12).reshape(3, 4)
print("\nМатрица из arange(12), reshape(3, 4):")
print(range_matrix)