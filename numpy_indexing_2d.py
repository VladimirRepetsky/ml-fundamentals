import numpy as np

matrix = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
])

print("Матрица:")
print(matrix)
print("Форма:", matrix.shape)

# === Базовая индексация ===
# Синтаксис: matrix[строка, столбец]

print("\n=== Базовая индексация ===")
print("Элемент [0, 0]:", matrix[0, 0])   # первый элемент
print("Элемент [0, 1]:", matrix[0, 1])   # второй элемент первой строки
print("Элемент [1, 2]:", matrix[1, 2])   # третий элемент второй строки
print("Элемент [2, 3]:", matrix[2, 3])   # последний элемент
print("Элемент [-1, -1]:", matrix[-1, -1])  # последний элемент (альтернатива)

# === Срезы строк и столбцов ===
# Синтаксис: matrix[start:stop, start:stop]

print("\n=== Срезы ===")
print("Первая строка:", matrix[0])
print("Первая строка (явно):", matrix[0, :])
print("Второй столбец:", matrix[:, 1])
print("Последний столбец:", matrix[:, -1])

# === Срезы диапазонов ===

print("\n=== Срезы диапазонов ===")
print("Первые две строки:")
print(matrix[:2])

print("Подматрица [0:2, 1:3]:")
print(matrix[0:2, 1:3])

print("Все строки, столбцы с 1 по 3:")
print(matrix[:, 1:4])

print("Каждый второй столбец:")
print(matrix[:, ::2])

print("Матрица в обратном порядке строк:")
print(matrix[::-1])

print("Матрица в обратном порядке строк и столбцов:")
print(matrix[::-1, ::-1])

# === Изменение элементов ===

print("\n=== Изменение элементов ===")
matrix2 = matrix.copy()
matrix2[0, 0] = 999
print("После matrix2[0, 0] = 999:")
print(matrix2)

matrix2[1] = [0, 0, 0, 0]
print("После matrix2[1] = [0, 0, 0, 0]:")
print(matrix2)

matrix2[:, 2] = -1
print("После matrix2[:, 2] = -1:")
print(matrix2)

# === Булева индексация для 2D ===

print("\n=== Булева индексация ===")
data = np.array([
    [12, -7, 5],
    [64, -1, 0],
    [33, 8, -15],
])

print("Матрица:")
print(data)

print("Элементы больше 10:", data[data > 10])
print("Положительные элементы:", data[data > 0])

# Маска
mask = data > 10
print("\nМаска (больше 10):")
print(mask)

# Замена по маске
data_copy = data.copy()
data_copy[data_copy < 0] = 0
print("\nПосле замены отрицательных на 0:")
print(data_copy)