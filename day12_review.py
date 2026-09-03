"""
Быстрое повторение ключевых алгоритмов Дня 11.
"""
import time


def linear_search(data, target):
    """Линейный поиск — O(n)."""
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1


def binary_search(data, target):
    """Бинарный поиск — O(log n). Требует отсортированных данных."""
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


def bubble_sort(data):
    """Пузырьковая сортировка — O(n²)."""
    data = data.copy()
    n = len(data)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        if not swapped:
            break
    return data


def selection_sort(data):
    """Сортировка выбором — O(n²)."""
    data = data.copy()
    n = len(data)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if data[j] < data[min_index]:
                min_index = j
        if min_index != i:
            data[i], data[min_index] = data[min_index], data[i]
    return data


# Тестирование
print("=" * 50)
print("Повторение Дня 11")
print("=" * 50)

numbers = [64, 34, 25, 12, 22, 11, 90]
print(f"\nИсходный: {numbers}")
print(f"Пузырьковая: {bubble_sort(numbers)}")
print(f"Выбором: {selection_sort(numbers)}")

sorted_data = list(range(1, 1001))
target = 999

idx1 = linear_search(sorted_data, target)
idx2 = binary_search(sorted_data, target)

print(f"\nЛинейный поиск {target}: индекс {idx1}")
print(f"Бинарный поиск {target}: индекс {idx2}")
print("\nВсё работает — идём дальше.")