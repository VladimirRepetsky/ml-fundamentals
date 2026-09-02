def binary_search(data, target):
    """
    Бинарный поиск элемента в ОТСОРТИРОВАННОМ списке.
    
    Возвращает индекс элемента, если найден, иначе -1.
    Сложность: O(log n)
    """
    left = 0
    right = len(data) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def binary_search_with_steps(data, target):
    """
    Бинарный поиск с подсчётом шагов и визуализацией.
    """
    left = 0
    right = len(data) - 1
    steps = 0
    
    print(f"  Ищем {target} в списке из {len(data)} элементов")
    
    while left <= right:
        steps += 1
        mid = (left + right) // 2
        
        print(f"  Шаг {steps}: диапазон [{left}..{right}], "
              f"середина = {mid}, значение = {data[mid]}")
        
        if data[mid] == target:
            print(f"  Найдено на позиции {mid} за {steps} шагов!")
            return mid, steps
        elif data[mid] < target:
            left = mid + 1
            print(f"    → {data[mid]} < {target}, идём вправо")
        else:
            right = mid - 1
            print(f"    → {data[mid]} > {target}, идём влево")
    
    print(f"  Не найдено. Шагов: {steps}")
    return -1, steps


def binary_search_recursive(data, target, left=0, right=None):
    """
    Рекурсивная версия бинарного поиска.
    Сложность: O(log n)
    """
    if right is None:
        right = len(data) - 1
    
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if data[mid] == target:
        return mid
    elif data[mid] < target:
        return binary_search_recursive(data, target, mid + 1, right)
    else:
        return binary_search_recursive(data, target, left, mid - 1)


# Тестирование
print("=" * 50)
print("Бинарный поиск")
print("=" * 50)

# ВАЖНО: данные должны быть отсортированы!
sorted_numbers = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91]

print(f"Отсортированный список: {sorted_numbers}")
print()

# Базовый поиск
for target in [23, 72, 1, 50, 91]:
    index = binary_search(sorted_numbers, target)
    if index != -1:
        print(f"Поиск {target}: найден на индексе {index}")
    else:
        print(f"Поиск {target}: не найден")

# Детальный поиск с шагами
print()
print("--- Детальный поиск ---")
large_data = list(range(1, 101))  # числа от 1 до 100

print()
binary_search_with_steps(large_data, 73)

print()
binary_search_with_steps(large_data, 1)

print()
binary_search_with_steps(large_data, 100)

# Рекурсивная версия
print()
print("--- Рекурсивная версия ---")
result = binary_search_recursive(sorted_numbers, 38)
print(f"Рекурсивный поиск 38: индекс = {result}")

# Сравнение шагов
print()
print("=" * 50)
print("Сравнение: линейный vs бинарный поиск")
print("=" * 50)

data = list(range(1, 1_000_001))  # миллион элементов
target = 999_999

# Линейный: ~999999 шагов (не будем запускать, слишком долго)
# Бинарный: ~20 шагов
index, steps = binary_search_with_steps(data, target)
print(f"\nДля массива из {len(data)} элементов:")
print(f"Бинарный поиск нашёл за {steps} шагов")
print(f"Линейный поиск потребовал бы до {len(data)} шагов")