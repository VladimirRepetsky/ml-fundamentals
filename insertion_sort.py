def insertion_sort(data):
    """
    Сортировка вставками.
    
    Берём каждый элемент и вставляем его в правильное место
    в уже отсортированной части массива.
    
    Сложность:
        Лучший случай: O(n) — массив уже отсортирован
        Средний случай: O(n²)
        Худший случай: O(n²) — массив в обратном порядке
    
    Устойчивая сортировка: не меняет порядок равных элементов.
    """
    data = data.copy()
    n = len(data)
    
    for i in range(1, n):
        key = data[i]  # Элемент, который нужно вставить
        j = i - 1
        
        # Сдвигаем элементы, которые больше key, вправо
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        
        # Вставляем key на правильное место
        data[j + 1] = key
    
    return data


def insertion_sort_with_steps(data):
    """
    Сортировка вставками с визуализацией шагов.
    """
    data = data.copy()
    n = len(data)
    total_comparisons = 0
    total_shifts = 0
    
    print(f"Исходный массив: {data}")
    print()
    
    for i in range(1, n):
        key = data[i]
        j = i - 1
        
        print(f"  Шаг {i}: берём элемент {key}")
        
        while j >= 0 and data[j] > key:
            total_comparisons += 1
            data[j + 1] = data[j]
            j -= 1
            total_shifts += 1
            print(f"    Сдвигаем {data[j + 1]} вправо → {data}")
        
        if j >= 0:
            total_comparisons += 1  # последнее сравнение, которое не сдвинуло
        
        data[j + 1] = key
        print(f"    Вставляем {key} на позицию {j + 1} → {data}")
        print()
    
    print(f"Итого: {total_comparisons} сравнений, {total_shifts} сдвигов")
    print(f"Результат: {data}")
    
    return data


def insertion_sort_desc(data):
    """
    Сортировка вставками по убыванию.
    """
    data = data.copy()
    n = len(data)
    
    for i in range(1, n):
        key = data[i]
        j = i - 1
        
        # Меняем условие: сдвигаем, если элемент МЕНЬШЕ key
        while j >= 0 and data[j] < key:
            data[j + 1] = data[j]
            j -= 1
        
        data[j + 1] = key
    
    return data


# Тестирование
print("=" * 50)
print("Сортировка вставками")
print("=" * 50)

# Базовая версия
numbers = [64, 34, 25, 12, 22, 11, 90]
print(f"\nИсходный: {numbers}")
result = insertion_sort(numbers)
print(f"Результат: {result}")

# По убыванию
print(f"\nПо убыванию: {insertion_sort_desc(numbers)}")

# Уже отсортированный массив — лучший случай
sorted_data = [1, 2, 3, 4, 5]
print(f"\nУже отсортированный: {sorted_data}")
result = insertion_sort(sorted_data)
print(f"Результат: {result}")
print("(В лучшем случае — O(n), потому что сдвигов нет)")

# Обратный порядок — худший случай
reversed_data = [5, 4, 3, 2, 1]
print(f"\nОбратный порядок: {reversed_data}")
result = insertion_sort(reversed_data)
print(f"Результат: {result}")
print("(В худшем случае — O(n²))")

# Детальная визуализация
print(f"\n--- Детальная визуализация ---")
small_data = [5, 3, 8, 1, 2]
insertion_sort_with_steps(small_data)