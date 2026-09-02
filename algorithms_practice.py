"""
Практические упражнения по алгоритмам.
"""

# ============================================================
# Упражнение 1: Бинарный поиск для поиска диапазона
# Найти первое и последнее вхождение элемента
# ============================================================

def find_first_and_last(data, target):
    """
    Находит первое и последнее вхождение target в отсортированном списке.
    Возвращает кортеж (first_index, last_index) или (-1, -1).
    """
    first = -1
    last = -1
    
    # Ищем первое вхождение
    left, right = 0, len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            first = mid
            right = mid - 1  # продолжаем искать левее
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    # Ищем последнее вхождение
    left, right = 0, len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            last = mid
            left = mid + 1  # продолжаем искать правее
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return first, last


# ============================================================
# Упражнение 2: Подсчёт инверсий при пузырьковой сортировке
# Инверсия — пара элементов, стоящих в неправильном порядке
# ============================================================

def count_inversions(data):
    """
    Подсчитывает количество инверсий в массиве.
    Инверсия: i < j, но data[i] > data[j].
    Сложность: O(n²) — наивный подход.
    """
    count = 0
    n = len(data)
    for i in range(n):
        for j in range(i + 1, n):
            if data[i] > data[j]:
                count += 1
    return count


# ============================================================
# Упражнение 3: Сортировка выбором по возрастанию/убыванию
# с параметром направления
# ============================================================

def selection_sort_direction(data, reverse=False):
    """
    Сортировка выбором с выбором направления.
    reverse=False → по возрастанию
    reverse=True → по убыванию
    """
    n = len(data)
    
    for i in range(n):
        target_index = i
        
        for j in range(i + 1, n):
            if not reverse:
                # Ищем минимум
                if data[j] < data[target_index]:
                    target_index = j
            else:
                # Ищем максимум
                if data[j] > data[target_index]:
                    target_index = j
        
        if target_index != i:
            data[i], data[target_index] = data[target_index], data[i]
    
    return data


# ============================================================
# Тестирование
# ============================================================

print("=" * 50)
print("Практические упражнения")
print("=" * 50)

# Упражнение 1
print("\n--- Упражнение 1: Первое и последнее вхождение ---")
data = [1, 2, 2, 2, 3, 4, 5, 5, 5, 5, 6]
for target in [2, 5, 7]:
    first, last = find_first_and_last(data, target)
    print(f"  {target}: первое={first}, последнее={last}")

# Упражнение 2
print("\n--- Упражнение 2: Подсчёт инверсий ---")
test_cases = [
    [1, 2, 3, 4, 5],   # 0 инверсий (отсортирован)
    [5, 4, 3, 2, 1],   # максимум инверсий
    [2, 4, 1, 3, 5],   # 3 инверсии
]
for tc in test_cases:
    inv = count_inversions(tc)
    print(f"  {tc} → {inv} инверсий")

# Упражнение 3
print("\n--- Упражнение 3: Сортировка с направлением ---")
data = [64, 25, 12, 22, 11]
print(f"  Исходный: {data}")
print(f"  По возрастанию: {selection_sort_direction(data.copy(), reverse=False)}")
print(f"  По убыванию: {selection_sort_direction(data.copy(), reverse=True)}")