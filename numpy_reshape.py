import numpy as np

# === reshape: изменение формы ===

arr = np.arange(12)
print("Исходный массив:", arr)
print("Форма:", arr.shape)

# Превращаем 1D массив из 12 элементов в матрицу 3x4
matrix_3x4 = arr.reshape(3, 4)
print("\nReshape(3, 4):")
print(matrix_3x4)
print("Форма:", matrix_3x4.shape)

# Превращаем в матрицу 4x3
matrix_4x3 = arr.reshape(4, 3)
print("\nReshape(4, 3):")
print(matrix_4x3)
print("Форма:", matrix_4x3.shape)

# Превращаем в матрицу 2x6
matrix_2x6 = arr.reshape(2, 6)
print("\nReshape(2, 6):")
print(matrix_2x6)
print("Форма:", matrix_2x6.shape)

# === Правило: количество элементов должно совпадать ===

# arr имеет 12 элементов
# Значит, можно сделать:
# reshape(3, 4) — 3*4 = 12 ✓
# reshape(2, 6) — 2*6 = 12 ✓
# reshape(1, 12) — 1*12 = 12 ✓
# reshape(12, 1) — 12*1 = 12 ✓
# reshape(3, 5) — 3*5 = 15 ✗ ОШИБКА

# === Использование -1 для автоматического вычисления ===

# Если одну из размерностей указать как -1,
# NumPy сам вычислит нужное значение
matrix_auto = arr.reshape(3, -1)
print("\nReshape(3, -1):")
print(matrix_auto)
print("Форма:", matrix_auto.shape)

matrix_auto2 = arr.reshape(-1, 4)
print("\nReshape(-1, 4):")
print(matrix_auto2)
print("Форма:", matrix_auto2.shape)

# === Из 2D обратно в 1D ===

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
])

print("\n=== Из 2D в 1D ===")
print("Исходная матрица:")
print(matrix)
print("Форма:", matrix.shape)

# Способ 1: flatten() — создаёт КОПИЮ
flat_copy = matrix.flatten()
print("\nflatten():", flat_copy)
print("Форма:", flat_copy.shape)

# Способ 2: ravel() — создаёт ПРЕДСТАВЛЕНИЕ (если возможно)
flat_view = matrix.ravel()
print("ravel():", flat_view)
print("Форма:", flat_view.shape)

# Способ 3: reshape(-1)
flat_reshape = matrix.reshape(-1)
print("reshape(-1):", flat_reshape)
print("Форма:", flat_reshape.shape)

# === Разница между flatten и ravel ===

print("\n=== Разница между flatten и ravel ===")

matrix = np.array([[1, 2], [3, 4]])

flat = matrix.flatten()
flat[0] = 999
print("После изменения flatten():")
print("flat:", flat)
print("Оригинал не изменился:", matrix)

matrix2 = np.array([[1, 2], [3, 4]])
rav = matrix2.ravel()
rav[0] = 999
print("\nПосле изменения ravel():")
print("ravel:", rav)
print("Оригинал изменился:", matrix2)

# === Изменение формы матрицы признаков ===
# Это очень важный приём в машинном обучении

print("\n=== Практический пример: матрица признаков ===")

# Допустим, у нас есть 6 образцов данных с 2 признаками
features_flat = np.array([25, 175, 30, 165, 35, 180, 28, 170, 22, 160, 40, 190])
print("Плоский массив:", features_flat)
print("Форма:", features_flat.shape)

# Превращаем в матрицу 6 образцов × 2 признака
features = features_flat.reshape(6, 2)
print("\nМатрица признаков:")
print(features)
print("Форма:", features.shape)
print("Каждая строка — один образец, каждый столбец — один признак")