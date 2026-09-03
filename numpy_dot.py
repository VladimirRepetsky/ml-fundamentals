import numpy as np

# === Скалярное произведение векторов ===

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("=== Скалярное произведение векторов ===")
print("a =", a)
print("b =", b)

# Способ 1: np.dot()
dot_result = np.dot(a, b)
print("np.dot(a, b):", dot_result)

# Способ 2: метод .dot()
dot_result2 = a.dot(b)
print("a.dot(b):", dot_result2)

# Способ 3: оператор @
dot_result3 = a @ b
print("a @ b:", dot_result3)

# Ручной расчёт: 1*4 + 2*5 + 3*6 = 4 + 10 + 18 = 32
print("Ручной расчёт: 1*4 + 2*5 + 3*6 =", 1*4 + 2*5 + 3*6)

# === Матричное умножение ===

print("\n=== Матричное умножение ===")

A = np.array([
    [1, 2, 3],
    [4, 5, 6],
])

B = np.array([
    [7, 8],
    [9, 10],
    [11, 12],
])

print("A:")
print(A)
print("A.shape:", A.shape)

print("\nB:")
print(B)
print("B.shape:", B.shape)

# Умножение: (2,3) @ (3,2) = (2,2)
C = A @ B
print("\nA @ B:")
print(C)
print("C.shape:", C.shape)

# Альтернатива:
C2 = np.dot(A, B)
print("\nnp.dot(A, B):")
print(C2)

# === Правило матричного умножения ===

print("\n=== Правило матричного умножения ===")
print("Чтобы умножить A на B:")
print("  Количество СТОЛБЦОВ A должно быть равно количеству СТРОК B")
print("  A.shape = (m, n), B.shape = (n, p)")
print("  Результат: (m, p)")
print()
print("Пример:")
print("  A.shape =", A.shape, "→ 2 строки, 3 столбца")
print("  B.shape =", B.shape, "→ 3 строки, 2 столбца")
print("  Столбцы A (3) == Строки B (3) ✓")
print("  Результат: (2, 2)")

# === Что будет, если размеры не совпадают ===

print("\n=== Попытка неправильного умножения ===")
try:
    # A имеет форму (2, 3), B имеет форму (3, 2)
    # B @ A = (3, 2) @ (2, 3) = (3, 3) — работает
    result = B @ A
    print("B @ A:")
    print(result)
    print("Форма:", result.shape)
    
    # Но если попробовать умножить матрицы с несовместимыми размерами:
    bad = np.array([[1, 2], [3, 4]])  # (2, 2)
    # A @ bad = (2, 3) @ (2, 2) — не работает, потому что 3 != 2
    result2 = A @ bad
except ValueError as e:
    print("Ошибка:", e)

# === Матрица на вектор ===

print("\n=== Матрица на вектор ===")

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
])

vector = np.array([10, 20, 30])

result = matrix @ vector
print("Матрица:")
print(matrix)
print("Вектор:", vector)
print("Результат (матрица @ вектор):", result)

# === Умножение на скаляр ===

print("\n=== Умножение на скаляр ===")
print("matrix * 2:")
print(matrix * 2)

print("\nmatrix + 10:")
print(matrix + 10)

# === Единичная матрица ===

print("\n=== Единичная матрица ===")
identity = np.eye(3)
A_square = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("A:")
print(A_square)
print("\nA @ I (умножение на единичную матрицу):")
print(A_square @ identity)
print("Результат равен A:", np.array_equal(A_square @ identity, A_square))

# === Матричное умножение в машинном обучении ===

print("\n=== Применение в машинном обучении ===")
print("В линейной регрессии предсказание выглядит так:")
print("  y_pred = X @ w")
print("где X — матрица признаков, w — вектор весов")
print()

# Пример: 3 образца, 2 признака
X = np.array([
    [1, 2],
    [3, 4],
    [5, 6],
])

# Веса модели
w = np.array([0.5, -1.0])

# Предсказания
y_pred = X @ w
print("X (матрица признаков):")
print(X)
print("w (веса):", w)
print("y_pred = X @ w:", y_pred)