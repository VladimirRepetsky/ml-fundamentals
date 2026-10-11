import numpy as np

print("=" * 60)
print("  SVD (СИНГУЛЯРНОЕ РАЗЛОЖЕНИЕ)")
print("=" * 60)

# === Исходная матрица ===
A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
])
print("\nИсходная матрица A:")
print(A)
print("Форма:", A.shape)

# === Выполняем SVD ===
U, s, Vt = np.linalg.svd(A)

print("\n=== Результат SVD: A = U · Σ · Vᵀ ===")
print(f"\nU (левые сингулярные векторы):")
print(U.round(4))
print("Форма U:", U.shape)

print(f"\ns (сингулярные числа):")
print(s.round(4))
print("Форма s:", s.shape)

print(f"\nVᵀ (правые сингулярные векторы, транспонированные):")
print(Vt.round(4))
print("Форма Vᵀ:", Vt.shape)

# === Восстанавливаем матрицу ===
# Σ — диагональная матрица из сингулярных чисел
Sigma = np.zeros(A.shape)
np.fill_diagonal(Sigma, s)

print("\nΣ (диагональная матрица сингулярных чисел):")
print(Sigma.round(4))

# Восстановление: A = U · Σ · Vᵀ
A_reconstructed = U @ Sigma @ Vt
print("\nВосстановленная матрица U · Σ · Vᵀ:")
print(A_reconstructed.round(4))

print("\nСовпадает с оригиналом:", np.allclose(A, A_reconstructed))

# === Свойства ===
print("\n" + "=" * 60)
print("  СВОЙСТВА")
print("=" * 60)
print(f"\nСингулярные числа: {s.round(4)}")
print("Они всегда неотрицательные и отсортированы по убыванию")
print("Проверка убывания:", all(s[i] >= s[i+1] for i in range(len(s)-1)))

# Доля «энергии» каждого сингулярного числа
total = np.sum(s ** 2)
print(f"\nДоля энергии каждого сингулярного числа:")
for i, sv in enumerate(s):
    energy = sv ** 2 / total * 100
    print(f"  σ_{i+1} = {sv:.4f} → {energy:.1f}% энергии")