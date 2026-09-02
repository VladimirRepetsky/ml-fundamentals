def bubble_sort(data):
    """
    Пузырьковая сортировка (базовая версия).
    
    Сложность: O(n²)
    """
    n = len(data)
    
    for i in range(n):
        for j in range(0, n - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    
    return data


def bubble_sort_optimized(data):
    """
    Оптимизированная пузырьковая сортировка.
    
    Если за проход не было обменов — массив уже отсортирован.
    Лучший случай: O(n)
    Худший случай: O(n²)
    """
    n = len(data)
    
    for i in range(n):
        swapped = False
        
        # Последние i элементов уже на месте
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        
        # Если обменов не было — массив отсортирован
        if not swapped:
            break
    
    return data


def bubble_sort_with_steps(data):
    """
    Пузырьковая сортировка с визуализацией шагов.
    """
    n = len(data)
    total_swaps = 0
    total_comparisons = 0
    
    print(f"Исходный массив: {data}")
    print()
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n - i - 1):
            total_comparisons += 1
            
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                total_swaps += 1
                swapped = True
                print(f"  Проход {i+1}: обмен {data[j+1]} и {data[j]} → {data}")
        
        if not swapped:
            print(f"  Проход {i+1}: обменов нет — массив отсортирован!")
            break
    
    print()
    print(f"Итого: {total_comparisons} сравнений, {total_swaps} обменов")
    print(f"Результат: {data}")
    
    return data


# Тестирование
print("=" * 50)
print("Пузырьковая сортировка")
print("=" * 50)

# Базовая версия
numbers = [64, 34, 25, 12, 22, 11, 90]
print(f"\nИсходный: {numbers}")
result = bubble_sort(numbers.copy())
print(f"Результат: {result}")

# Оптимизированная версия
print(f"\n--- Оптимизированная версия ---")
numbers = [64, 34, 25, 12, 22, 11, 90]
print(f"Исходный: {numbers}")
result = bubble_sort_optimized(numbers.copy())
print(f"Результат: {result}")

# Уже отсортированный массив
print(f"\n--- Уже отсортированный массив ---")
sorted_data = [1, 2, 3, 4, 5]
print(f"Исходный: {sorted_data}")
result = bubble_sort_optimized(sorted_data.copy())
print(f"Результат: {result}")
print("(Оптимизация останавливается после первого прохода)")

# Детальная визуализация
print(f"\n--- Детальная визуализация ---")
small_data = [5, 3, 8, 1, 2]
bubble_sort_with_steps(small_data.copy())

# Сравнение количества операций
print(f"\n--- Сравнение операций ---")
import time

sizes = [100, 500, 1000, 2000]

for size in sizes:
    data = list(range(size, 0, -1))  # обратный порядок — худший случай
    
    start = time.time()
    bubble_sort_optimized(data.copy())
    elapsed = (time.time() - start) * 1000
    
    print(f"Размер {size}: {elapsed:.2f} мс")

print()
print("Видно квадратичный рост: при увеличении размера в 2 раза")
print("время растёт примерно в 4 раза.")