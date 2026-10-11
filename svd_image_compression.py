"""
Применение SVD: сжатие изображений.
Наглядная демонстрация снижения размерности.
"""
import numpy as np

print("=" * 60)
print("  СЖАТИЕ ИЗОБРАЖЕНИЙ ЧЕРЕЗ SVD")
print("=" * 60)

# === Создаём синтетическое «изображение» ===
# Это матрица 50×50 с градиентом и паттерном
size = 50
image = np.zeros((size, size))

# Градиент по диагонали
for i in range(size):
    for j in range(size):
        image[i, j] = (i + j) / (2 * size)

# Добавляем паттерн (синусоиду)
for i in range(size):
    image[i, :] += 0.3 * np.sin(np.linspace(0, 4 * np.pi, size))

print(f"\nИсходное «изображение» {size}×{size}")
print(f"Всего значений: {size * size}")
print(f"Минимум: {image.min():.4f}, Максимум: {image.max():.4f}")

# === SVD ===
U, s, Vt = np.linalg.svd(image, full_matrices=False)

print(f"\nСингулярных чисел: {len(s)}")
print(f"Первые 10: {s[:10].round(4)}")

# === Доля энергии ===
total_energy = np.sum(s ** 2)
print("\nНакопительная доля энергии:")
cumulative = 0
for k in [1, 2, 3, 5, 10, 20, 50]:
    if k <= len(s):
        energy = np.sum(s[:k] ** 2) / total_energy * 100
        print(f"  k={k:>2}: {energy:.2f}%")

# === Сжатие ===
def compress_image(matrix, k):
    """Сжимает изображение, оставляя k сингулярных чисел."""
    U, s, Vt = np.linalg.svd(matrix, full_matrices=False)
    U_k = U[:, :k]
    s_k = np.diag(s[:k])
    Vt_k = Vt[:k, :]
    compressed = U_k @ s_k @ Vt_k
    return compressed

print("\n" + "=" * 60)
print("  СЖАТИЕ С РАЗНЫМ k")
print("=" * 60)

for k in [1, 2, 5, 10, 20]:
    compressed = compress_image(image, k)
    
    # Считаем размер хранения
    # Оригинал: size × size значений
    # Сжатое: size×k + k + k×size значений
    original_size = size * size
    compressed_size = size * k + k + k * size
    compression_ratio = original_size / compressed_size
    
    # Ошибка сжатия (MSE)
    mse = np.mean((image - compressed) ** 2)
    
    print(f"\nk={k}:")
    print(f"  Размер хранения: {compressed_size} вместо {original_size}")
    print(f"  Коэффициент сжатия: {compression_ratio:.2f}x")
    print(f"  MSE (ошибка): {mse:.6f}")

print("\n" + "=" * 60)
print("  ВЫВОД")
print("=" * 60)
print("""
Чем больше k, тем:
  + выше качество изображения
  − больше места для хранения

Чем меньше k, тем:
  + сильнее сжатие
  − больше теряется деталей

В реальных задачах выбирают k так, чтобы сохранить
95-99% энергии (дисперсии).

Это и есть компромисс между размером и качеством,
который лежит в основе сжатия данных.
""")