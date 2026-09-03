"""
Демонстрация устойчивости сортировок.

Устойчивая сортировка сохраняет порядок равных элементов.
"""


def bubble_sort_stable(data, key_func=None):
    """Пузырьковая сортировка — УСТОЙЧИВАЯ."""
    data = data.copy()
    n = len(data)
    
    if key_func is None:
        key_func = lambda x: x
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if key_func(data[j]) > key_func(data[j + 1]):
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        if not swapped:
            break
    return data


def selection_sort_unstable(data, key_func=None):
    """Сортировка выбором — НЕУСТОЙЧИВАЯ."""
    data = data.copy()
    n = len(data)
    
    if key_func is None:
        key_func = lambda x: x
    
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if key_func(data[j]) < key_func(data[min_index]):
                min_index = j
        if min_index != i:
            data[i], data[min_index] = data[min_index], data[i]
    return data


def insertion_sort_stable(data, key_func=None):
    """Сортировка вставками — УСТОЙЧИВАЯ."""
    data = data.copy()
    n = len(data)
    
    if key_func is None:
        key_func = lambda x: x
    
    for i in range(1, n):
        key_item = data[i]
        key_val = key_func(key_item)
        j = i - 1
        
        while j >= 0 and key_func(data[j]) > key_val:
            data[j + 1] = data[j]
            j -= 1
        
        data[j + 1] = key_item
    
    return data


# Демонстрация
print("=" * 55)
print("  УСТОЙЧИВОСТЬ СОРТИРОВОК")
print("=" * 55)

# Создаём данные с одинаковыми ключами
# Формат: (оценка, имя_студента)
students = [
    (85, "Alice"),
    (92, "Bob"),
    (85, "Charlie"),
    (92, "David"),
    (85, "Eve"),
]

print(f"\nИсходные данные:")
for grade, name in students:
    print(f"  Оценка {grade}: {name}")

print(f"\nСортируем по оценке (по возрастанию):")
print()

# Пузырьковая — устойчивая
result = bubble_sort_stable(students, key_func=lambda x: x[0])
print("  Пузырьковая (УСТОЙЧИВАЯ):")
for grade, name in result:
    print(f"    Оценка {grade}: {name}")
print("  → Alice, Charlie, Eve сохранили свой порядок среди оценки 85")
print("  → Bob, David сохранили свой порядок среди оценки 92")

print()

# Выбором — НЕ устойчивая
result = selection_sort_unstable(students, key_func=lambda x: x[0])
print("  Выбором (НЕУСТОЙЧИВАЯ):")
for grade, name in result:
    print(f"    Оценка {grade}: {name}")
print("  → Порядок равных элементов МОГ измениться")

print()

# Вставками — устойчивая
result = insertion_sort_stable(students, key_func=lambda x: x[0])
print("  Вставками (УСТОЙЧИВАЯ):")
for grade, name in result:
    print(f"    Оценка {grade}: {name}")
print("  → Порядок равных элементов сохранился")

print()

# Встроенная sorted() — устойчивая (Timsort)
result = sorted(students, key=lambda x: x[0])
print("  sorted() / Timsort (УСТОЙЧИВАЯ):")
for grade, name in result:
    print(f"    Оценка {grade}: {name}")

print()
print("=" * 55)
print("  ВЫВОД")
print("=" * 55)
print()
print("  Устойчивые:     пузырьковая, вставками, Timsort")
print("  Неустойчивые:   выбором")
print()
print("  В продакшене sorted() всегда устойчива.")
print("  Это важно, когда сортируешь по нескольким критериям:")
print("  сначала по дате, потом по имени — порядок не ломается.")