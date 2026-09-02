def selection_sort(data):
    """
    Сортировка выбором.
    
    На каждом шаге находим минимум в оставшейся части
    и ставим его на текущую позицию.
    
    Сложность: O(n²)
    """
    n = len(data)
    
    for i in range(n):
        # Предполагаем, что минимальный элемент — текущий
        min_index = i
        
        # Ищем минимальный элемент в оставшейся части
        for j in range(i + 1, n):
            if data[j] < data[min_index]:
                min_index = j
        
        # Меняем местами текущий и минимальный
        if min_index != i:
            data[i], data[min_index] = data[min_index], data[i]
    
    return data


def selection_sort_with_steps(data):
    """
    Сортировка выбором с визуализацией.
    """
    n = len(data)
    total_comparisons = 0
    total_swaps = 0
    
    print(f"Исходный массив: {data}")
    print()
    
    for i in range(n):
        min_index = i
        
        for j in range(i + 1, n):
            total_comparisons += 1
            if data[j] < data[min_index]:
                min_index = j
        
        if min_index != i:
            data[i], data[min_index] = data[min_index], data[i]
            total_swaps += 1
            print(f"  Шаг {i+1}: нашёл минимум {data[i]} на позиции {min_index}, "
                  f"поменял с позицией {i} → {data}")
        else:
            print(f"  Шаг {i+1}: элемент {data[i]} уже на месте")
    
    print()
    print(f"Итого: {total_comparisons} сравнений, {total_swaps} обменов")
    print(f"Результат: {data}")
    
    return data


def selection_sort_desc(data):
    """
    Сортировка выбором по убыванию.
    """
    n = len(data)
    
    for i in range(n):
        max_index = i
        
        for j in range(i + 1, n):
            if data[j] > data[max_index]:
                max_index = j
        
        if max_index != i:
            data[i], data[max_index] = data[max_index], data[i]
    
    return data


# Тестирование
print("=" * 50)
print("Сортировка выбором")
print("=" * 50)

# Базовая версия
numbers = [64, 25, 12, 22, 11]
print(f"\nИсходный: {numbers}")
result = selection_sort(numbers.copy())
print(f"Результат: {result}")

# По убыванию
numbers = [64, 25, 12, 22, 11]
print(f"\nПо убыванию: {numbers}")
result = selection_sort_desc(numbers.copy())
print(f"Результат: {result}")

# Детальная визуализация
print(f"\n--- Детальная визуализация ---")
small_data = [29, 10, 14, 37, 13]
selection_sort_with_steps(small_data.copy())

# Сравнение с пузырьковой
print(f"\n--- Сравнение с пузырьковой ---")
import time

data = list(range(1000, 0, -1))

start = time.time()
selection_sort(data.copy())
selection_time = (time.time() - start) * 1000

# Импортируем пузырьковую из соседнего файла
from bubble_sort import bubble_sort_optimized

start = time.time()
bubble_sort_optimized(data.copy())
bubble_time = (time.time() - start) * 1000

print(f"Сортировка выбором: {selection_time:.2f} мс")
print(f"Пузырьковая сортировка: {bubble_time:.2f} мс")
print()
print("Обе имеют сложность O(n²), но константы различаются.")