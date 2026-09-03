import numpy as np

# === Создание массивов ===

# Из списка
numbers = np.array([1, 2, 3, 4, 5])
print("Массив из списка:", numbers)
print("Тип:", type(numbers))

# Из списка с плавающей точкой
floats = np.array([1.0, 2.5, 3.7, 4.0])
print("Массив из float:", floats)

# Массив нулей
zeros = np.zeros(5)
print("Нули:", zeros)

# Массив единиц
ones = np.ones(5)
print("Единицы:", ones)

# Массив чисел от 0 до 4
range_arr = np.arange(5)
print("arange(5):", range_arr)

# Массив чисел от 1 до 10
range_arr2 = np.arange(1, 11)
print("arange(1, 11):", range_arr2)

# Массив чисел от 0 до 10 с шагом 2
range_arr3 = np.arange(0, 11, 2)
print("arange(0, 11, 2):", range_arr3)

# Массив с равномерными точками между 0 и 1
linspace_arr = np.linspace(0, 1, 5)
print("linspace(0, 1, 5):", linspace_arr)

# Массив со случайными числами от 0 до 1
random_arr = np.random.random(5)
print("random(5):", random_arr)

# Массив со случайными целыми числами от 1 до 10
random_int_arr = np.random.randint(1, 11, size=5)
print("randint(1, 11, 5):", random_int_arr)

print("\n=== Свойства массивов ===")

arr = np.array([10, 20, 30, 40, 50])

print("Массив:", arr)
print("Форма (shape):", arr.shape)
print("Размерность (ndim):", arr.ndim)
print("Количество элементов (size):", arr.size)
print("Тип данных элементов (dtype):", arr.dtype)
print("Размер в байтах на элемент (itemsize):", arr.itemsize)
print("Общий размер в байтах (nbytes):", arr.nbytes)