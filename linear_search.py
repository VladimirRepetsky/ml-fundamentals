def linear_search(data, target):
    """
    Линейный поиск элемента в списке.
    
    Возвращает индекс элемента, если найден, иначе -1.
    Сложность: O(n)
    """
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1


def linear_search_all(data, target):
    """
    Находит ВСЕ индексы элемента в списке.
    
    Возвращает список индексов.
    Сложность: O(n)
    """
    indices = []
    for i in range(len(data)):
        if data[i] == target:
            indices.append(i)
    return indices


def linear_search_with_steps(data, target):
    """
    Линейный поиск с подсчётом шагов.
    Показывает, сколько сравнений потребовалось.
    """
    steps = 0
    for i in range(len(data)):
        steps += 1
        if data[i] == target:
            return i, steps
    return -1, steps


# Тестирование
numbers = [64, 34, 25, 12, 22, 11, 90, 34, 56]

print("=" * 50)
print("Линейный поиск")
print("=" * 50)
print(f"Список: {numbers}")
print()

# Поиск существующего элемента
target = 22
index = linear_search(numbers, target)
print(f"Поиск {target}: индекс = {index}")

# Поиск несуществующего элемента
target = 99
index = linear_search(numbers, target)
print(f"Поиск {target}: индекс = {index} (не найден)")

# Поиск всех вхождений
target = 34
indices = linear_search_all(numbers, target)
print(f"Все вхождения {target}: индексы = {indices}")

# Подсчёт шагов
print()
print("--- Подсчёт шагов ---")
data = list(range(1, 101))  # числа от 1 до 100

for target in [1, 50, 100, 999]:
    index, steps = linear_search_with_steps(data, target)
    if index != -1:
        print(f"Поиск {target}: найден на позиции {index}, шагов: {steps}")
    else:
        print(f"Поиск {target}: не найден, шагов: {steps}")

print()
print("Вывод: в худшем случае линейный поиск делает n шагов.")
print("Это и есть O(n).")