import numpy as np

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90],
])

print("Матрица:")
print(matrix)
print("Форма:", matrix.shape)

# === Агрегация без указания оси ===

print("\n=== Без оси ===")
print("np.sum(matrix):", np.sum(matrix))
print("np.mean(matrix):", np.mean(matrix))
print("np.max(matrix):", np.max(matrix))
print("np.min(matrix):", np.min(matrix))

# === Агрегация по оси 0 (вдоль строк) ===
# Результат: одно значение на каждый СТОЛБЕЦ

print("\n=== axis=0 (по столбцам) ===")
print("np.sum(matrix, axis=0):", np.sum(matrix, axis=0))
print("np.mean(matrix, axis=0):", np.mean(matrix, axis=0))
print("np.max(matrix, axis=0):", np.max(matrix, axis=0))
print("np.min(matrix, axis=0):", np.min(matrix, axis=0))

# === Агрегация по оси 1 (вдоль столбцов) ===
# Результат: одно значение на каждую СТРОКУ

print("\n=== axis=1 (по строкам) ===")
print("np.sum(matrix, axis=1):", np.sum(matrix, axis=1))
print("np.mean(matrix, axis=1):", np.mean(matrix, axis=1))
print("np.max(matrix, axis=1):", np.max(matrix, axis=1))
print("np.min(matrix, axis=1):", np.min(matrix, axis=1))

# === Практический пример: данные о людях ===

print("\n=== Практический пример ===")

# Данные: возраст, рост, вес для 4 человек
people = np.array([
    [25, 175, 70],
    [30, 165, 55],
    [35, 180, 85],
    [28, 170, 60],
])

print("Данные (возраст, рост, вес):")
print(people)

# Среднее по каждому признаку (по столбцам)
mean_per_feature = np.mean(people, axis=0)
print("\nСреднее по каждому признаку (axis=0):")
print(f"  Возраст: {mean_per_feature[0]:.1f}")
print(f"  Рост:    {mean_per_feature[1]:.1f}")
print(f"  Вес:     {mean_per_feature[2]:.1f}")

# Среднее по каждому человеку (по строкам)
mean_per_person = np.mean(people, axis=1)
print("\nСреднее по каждому человеку (axis=1):")
for i, value in enumerate(mean_per_person):
    print(f"  Человек {i+1}: {value:.1f}")

# Максимальное значение каждого признака
max_per_feature = np.max(people, axis=0)
print("\nМаксимум по каждому признаку (axis=0):")
print(f"  Возраст: {max_per_feature[0]}")
print(f"  Рост:    {max_per_feature[1]}")
print(f"  Вес:     {max_per_feature[2]}")

# Стандартное отклонение каждого признака
std_per_feature = np.std(people, axis=0)
print("\nСтандартное отклонение по каждому признаку (axis=0):")
print(f"  Возраст: {std_per_feature[0]:.2f}")
print(f"  Рост:    {std_per_feature[1]:.2f}")
print(f"  Вес:     {std_per_feature[2]:.2f}")

# === Нормализация и стандартизация по столбцам ===

print("\n=== Нормализация по столбцам ===")

# Нормализация: (x - min) / (max - min)
min_per_feature = np.min(people, axis=0)
max_per_feature = np.max(people, axis=0)
normalized = (people - min_per_feature) / (max_per_feature - min_per_feature)

print("Исходные данные:")
print(people)
print("\nНормализованные данные (каждый признак в [0, 1]):")
print(np.round(normalized, 3))

print("\n=== Стандартизация по столбцам ===")

# Стандартизация: (x - mean) / std
mean_per_feature = np.mean(people, axis=0)
std_per_feature = np.std(people, axis=0)
standardized = (people - mean_per_feature) / std_per_feature

print("Стандартизированные данные (среднее 0, стд 1):")
print(np.round(standardized, 3))

# Проверка
print("\nПроверка стандартизации:")
print("Среднее по столбцам:", np.round(np.mean(standardized, axis=0), 10))
print("Стд по столбцам:", np.round(np.std(standardized, axis=0), 10))