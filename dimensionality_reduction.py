"""
Концепция снижения размерности.
Объединяет идеи собственных значений и SVD.
"""
import numpy as np

print("=" * 60)
print("  КОНЦЕПЦИЯ СНИЖЕНИЯ РАЗМЕРНОСТИ")
print("=" * 60)

# === Зачем снижать размерность? ===
print("""
Проблема «проклятия размерности»:
  - Чем больше признаков, тем больше данных нужно для обучения.
  - Многие признаки избыточны или скоррелированы.
  - Модели становятся медленными и переобучаются.

Решение:
  - Оставить только самые информативные признаки.
  - Спроецировать данные в пространство меньшей размерности.

Методы:
  - PCA (через собственные значения ковариационной матрицы)
  - SVD (сингулярное разложение)
  - Автоэнкодеры (нейросетевой подход)
""")

# === Генерируем многомерные данные ===
np.random.seed(42)
n_samples = 200

# Данные лежат на 2D плоскости, вложенной в 5D пространство
t1 = np.random.randn(n_samples)
t2 = np.random.randn(n_samples)
# 5 признаков — линейные комбинации двух скрытых факторов
data = np.column_stack([
    t1 * 2 + t2 * 1,
    t1 * 1 + t2 * 2,
    t1 * 3 - t2 * 1,
    t1 * 1 - t2 * 2,
    t1 * 2 + t2 * 3,
]) + np.random.randn(n_samples, 5) * 0.5

print("=" * 60)
print("  ПРИМЕР: 5D ДАННЫЕ С 2 СКРЫТЫМИ ФАКТОРАМИ")
print("=" * 60)
print(f"\nИсходные данные: {data.shape}")
print("Фактически данные лежат на 2D плоскости в 5D пространстве")

# === Шаг 1: центрирование ===
data_centered = data - np.mean(data, axis=0)

# === Шаг 2: SVD ===
U, s, Vt = np.linalg.svd(data_centered, full_matrices=False)

print(f"\nСингулярные числа: {s.round(4)}")

# === Шаг 3: доля объяснённой дисперсии ===
total = np.sum(s ** 2)
print("\nДоля объяснённой дисперсии по компонентам:")
cumulative = 0
for i, sv in enumerate(s):
    explained = sv ** 2 / total * 100
    cumulative += explained
    print(f"  Компонента {i+1}: {explained:>5.1f}% (накопительно: {cumulative:>5.1f}%)")

# === Шаг 4: выбираем количество компонент ===
# Правило: выбираем k так, чтобы сохранить >= 95% дисперсии
target_variance = 0.95
cumulative = 0
k_chosen = 0
for i, sv in enumerate(s):
    cumulative += sv ** 2 / total
    if cumulative >= target_variance:
        k_chosen = i + 1
        break

print(f"\nДля сохранения {target_variance*100:.0f}% дисперсии нужно k={k_chosen} компонент")

# === Шаг 5: проекция данных ===
# Проецируем данные на первые k правых сингулярных векторов
V_k = Vt[:k_chosen, :].T  # (n_features, k)
data_projected = data_centered @ V_k

print(f"\nПроецированные данные: {data_projected.shape}")
print(f"Размерность снижена с {data.shape[1]} до {data_projected.shape[1]}")

# === Шаг 6: восстановление ===
# Можем восстановить приближённые исходные данные
data_reconstructed = data_projected @ V_k.T + np.mean(data, axis=0)

# Ошибка восстановления
mse = np.mean((data - data_reconstructed) ** 2)
print(f"\nОшибка восстановления (MSE): {mse:.6f}")
print("Маленькая ошибка = данные хорошо описываются 2 компонентами")

# === Итоги ===
print("\n" + "=" * 60)
print("  ИТОГИ")
print("=" * 60)
print(f"""
✅ Исходная размерность: {data.shape[1]} признаков
✅ После снижения: {data_projected.shape[1]} признака
✅ Сохранено дисперсии: {np.sum(s[:k_chosen]**2)/total*100:.1f}%
✅ Сжатие в {data.shape[1] / data_projected.shape[1]:.1f} раз

Это основа метода главных компонент (PCA).
В scikit-learn это реализовано как:
    from sklearn.decomposition import PCA
    pca = PCA(n_components=2)
    data_2d = pca.fit_transform(data)
""")