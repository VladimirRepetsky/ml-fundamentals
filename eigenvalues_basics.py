import numpy as np

# ============================================================
# СОБСТВЕННЫЕ ЗНАЧЕНИЯ И ВЕКТОРЫ
# ============================================================

print("=" * 60)
print("  СОБСТВЕННЫЕ ЗНАЧЕНИЯ И ВЕКТОРЫ")
print("=" * 60)

# === Простой пример ===
# Матрица растяжения
A = np.array([
    [2, 0],
    [0, 3]
])

print("\n=== Пример 1: Матрица растяжения ===")
print("A =")
print(A)
print("Эта матрица растягивает ось X в 2 раза, ось Y в 3 раза")

# Вычисляем собственные значения и векторы
eigenvalues, eigenvectors = np.linalg.eig(A)

print(f"\nСобственные значения: {eigenvalues}")
print("Собственные векторы (столбцы матрицы):")
print(eigenvectors)

# === Проверка: A·v = λ·v ===
print("\n=== Проверка: A·v = λ·v ===")
for i in range(len(eigenvalues)):
    v = eigenvectors[:, i]          # i-й собственный вектор (столбец)
    lam = eigenvalues[i]            # i-е собственное значение
    
    left_side = A @ v               # A · v
    right_side = lam * v            # λ · v
    
    print(f"\nСобственный вектор {i+1}: {v}")
    print(f"Собственное значение: {lam}")
    print(f"  A·v = {left_side}")
    print(f"  λ·v = {right_side}")
    print(f"  Совпадают: {np.allclose(left_side, right_side)}")

# === Пример 2: более сложная матрица ===
print("\n" + "=" * 60)
print("=== Пример 2: Не диагональная матрица ===")
B = np.array([
    [4, 1],
    [2, 3]
])
print("B =")
print(B)

eigenvalues_b, eigenvectors_b = np.linalg.eig(B)
print(f"\nСобственные значения: {eigenvalues_b}")
print("Собственные векторы (столбцы):")
print(eigenvectors_b)

# Проверка
print("\n=== Проверка ===")
for i in range(len(eigenvalues_b)):
    v = eigenvectors_b[:, i]
    lam = eigenvalues_b[i]
    left = B @ v
    right = lam * v
    print(f"Вектор {v}, λ={lam:.4f}: A·v ≈ λ·v: {np.allclose(left, right)}")

# === Пример 3: симметричная матрица ===
print("\n" + "=" * 60)
print("=== Пример 3: Симметричная матрица (как в PCA) ===")
# Ковариационные матрицы всегда симметричные
C = np.array([
    [4, 2],
    [2, 3]
])
print("C =")
print(C)
print("Симметричная: C == C.T:", np.array_equal(C, C.T))

eigenvalues_c, eigenvectors_c = np.linalg.eig(C)
print(f"\nСобственные значения: {eigenvalues_c}")
print("Собственные векторы (столбцы):")
print(eigenvectors_c)

# У симметричных матриц собственные векторы ортогональны
print("\nПроверка ортогональности собственных векторов:")
v1 = eigenvectors_c[:, 0]
v2 = eigenvectors_c[:, 1]
dot_product = np.dot(v1, v2)
print(f"  v1 · v2 = {dot_product:.6f}")
print(f"  (Должно быть ~0 для ортогональных векторов)")