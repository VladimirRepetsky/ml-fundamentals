import numpy as np

# Повторение базовых операций Дня 13
arr = np.array([10, 20, 30, 40, 50])

print("Массив:", arr)
print("Форма:", arr.shape)
print("Размерность:", arr.ndim)
print("Тип:", arr.dtype)

# Векторные операции
print("\nВекторные операции:")
print("arr * 2 =", arr * 2)
print("arr + 10 =", arr + 10)
print("arr ** 2 =", arr ** 2)

# Агрегации
print("\nАгрегации:")
print("np.sum:", np.sum(arr))
print("np.mean:", np.mean(arr))
print("np.max:", np.max(arr))

# Булева индексация
data = np.array([12, -7, 5, 64, -1, 0, 33, 8])
print("\nФильтрация:")
print("Положительные:", data[data > 0])
print("Между 0 и 30:", data[(data >= 0) & (data <= 30)])

# Евклидово расстояние из Дня 13
def euclidean_distance(a, b):
    return np.sqrt(np.sum((a - b) ** 2))

point_a = np.array([1, 2, 3])
point_b = np.array([4, 6, 3])
print("\nЕвклидово расстояние:", euclidean_distance(point_a, point_b))

print("\nВсё работает — идём дальше.")