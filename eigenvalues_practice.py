"""
Применение собственных значений: главные направления данных.
Это основа метода главных компонент (PCA).
"""
import numpy as np

print("=" * 60)
print("  ГЛАВНЫЕ НАПРАВЛЕНИЯ ДАННЫХ")
print("=" * 60)

# === Генерируем данные ===
# Создаём 2D данные, вытянутые вдоль определённого направления
np.random.seed(42)
n_points = 100

# Данные вытянуты вдоль направления (1, 2)
t = np.random.randn(n_points)
noise = np.random.randn(n_points, 2) * 0.3
data = np.column_stack([t * 1, t * 2]) + noise

print(f"\nСгенерировано {n_points} точек")
print("Данные вытянуты вдоль направления (1, 2)")
print("Среднее по столбцам:", np.mean(data, axis=0).round(3))

# === Шаг 1: центрируем данные ===
# Вычитаем среднее из каждого столбца
data_centered = data - np.mean(data, axis=0)
print("\nПосле центрирования:")
print("Среднее по столбцам:", np.mean(data_centered, axis=0).round(10))

# === Шаг 2: вычисляем ковариационную матрицу ===
# Ковариационная матрица показывает, как признаки связаны друг с другом
cov_matrix = np.cov(data_centered.T)
print("\nКовариационная матрица:")
print(cov_matrix.round(4))
print("Симметричная:", np.array_equal(cov_matrix, cov_matrix.T))

# === Шаг 3: находим собственные значения и векторы ===
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
print("\nСобственные значения:", eigenvalues.round(4))
print("Собственные векторы (столбцы):")
print(eigenvectors.round(4))

# === Шаг 4: сортируем по убыванию собственного значения ===
# Наибольшее собственное значение = направление максимальной дисперсии
sorted_indices = np.argsort(eigenvalues)[::-1]
eigenvalues_sorted = eigenvalues[sorted_indices]
eigenvectors_sorted = eigenvectors[:, sorted_indices]

print("\nОтсортировано по убыванию:")
print("Собственные значения:", eigenvalues_sorted.round(4))
print("Собственные векторы (столбцы):")
print(eigenvectors_sorted.round(4))

# === Шаг 5: интерпретация ===
print("\n" + "=" * 60)
print("  ИНТЕРПРЕТАЦИЯ")
print("=" * 60)

total_variance = np.sum(eigenvalues_sorted)
print(f"\nОбщая дисперсия: {total_variance:.4f}")

for i in range(len(eigenvalues_sorted)):
    explained = eigenvalues_sorted[i] / total_variance * 100
    print(f"\nГлавная компонента {i+1}:")
    print(f"  Собственное значение: {eigenvalues_sorted[i]:.4f}")
    print(f"  Объясняет дисперсии: {explained:.1f}%")
    print(f"  Направление: {eigenvectors_sorted[:, i].round(4)}")

print(f"\nПервая главная компонента объясняет "
      f"{eigenvalues_sorted[0]/total_variance*100:.1f}% дисперсии")
print("Это и есть направление максимальной вариации данных!")
print("\nОригинальное направление данных было (1, 2), нормированное:")
original_dir = np.array([1, 2]) / np.linalg.norm([1, 2])
print(f"  {original_dir.round(4)}")
print("Первый собственный вектор должен быть близок к этому направлению.")