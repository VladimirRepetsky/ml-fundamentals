import numpy as np

# === Базовая индексация ===

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print("Массив:", arr)
print("Первый элемент:", arr[0])
print("Второй элемент:", arr[1])
print("Последний элемент:", arr[-1])
print("Предпоследний элемент:", arr[-2])

# === Срезы ===
# Синтаксис: arr[start:stop:step]

print("\nСрезы:")
print("Первые 3 элемента:", arr[:3])
print("Элементы с 2 по 5:", arr[2:6])
print("Каждый второй:", arr[::2])
print("Каждый третий:", arr[::3])
print("В обратном порядке:", arr[::-1])
print("Последние 3 элемента:", arr[-3:])

# === Изменение элементов ===

arr2 = np.array([1, 2, 3, 4, 5])
print("\nИсходный:", arr2)

arr2[0] = 100
print("После arr2[0] = 100:", arr2)

arr2[1:4] = 0
print("После arr2[1:4] = 0:", arr2)

# === Копирование ===

# ВАЖНО: срез создаёт представление (view), а не копию!
original = np.array([1, 2, 3, 4, 5])
slice_view = original[1:4]

print("\n=== Копирование ===")
print("Оригинал:", original)
print("Срез:", slice_view)

slice_view[0] = 999
print("После изменения среза:")
print("Срез:", slice_view)
print("Оригинал:", original)  # Оригинал тоже изменился!

# Чтобы создать независимую копию:
original2 = np.array([1, 2, 3, 4, 5])
copy_arr = original2[1:4].copy()

copy_arr[0] = 999
print("\nПосле изменения копии:")
print("Копия:", copy_arr)
print("Оригинал:", original2)  # Оригинал не изменился

# === Булева индексация (маски) ===

numbers = np.array([12, -7, 5, 64, -1, 0, 33, 8])

print("\n=== Булева индексация ===")
print("Массив:", numbers)

# Маска: какие элементы положительные
positive_mask = numbers > 0
print("Маска (положительные):", positive_mask)

# Применение маски
positive_numbers = numbers[positive_mask]
print("Положительные:", positive_numbers)

# Отрицательные
negative_numbers = numbers[numbers < 0]
print("Отрицательные:", negative_numbers)

# Чётные
even_numbers = numbers[numbers % 2 == 0]
print("Чётные:", even_numbers)

# Элементы больше 10
big_numbers = numbers[numbers > 10]
print("Больше 10:", big_numbers)

# Комбинированные условия (используем & и |, а не and и or!)
result = numbers[(numbers > 0) & (numbers < 30)]
print("Между 0 и 30:", result)

# === Индексация по списку индексов ===

indices = [0, 3, 5, 7]
selected = numbers[indices]
print("\nПо индексам [0, 3, 5, 7]:", selected)

# То же самое через массив индексов
indices_arr = np.array([0, 3, 5, 7])
selected2 = numbers[indices_arr]
print("То же через массив:", selected2)