"""
Сравнение трёх простых сортировок:
- Пузырьковая
- Выбором
- Вставками

Тестируем на разных типах данных.
"""
import time
from bubble_sort import bubble_sort_optimized
from selection_sort import selection_sort
from insertion_sort import insertion_sort


def measure_time(func, data, label):
    """Измеряет время выполнения сортировки."""
    start = time.time()
    result = func(data)
    elapsed = (time.time() - start) * 1000  # миллисекунды
    return elapsed, result


def run_comparison(size, data_type="random"):
    """Запускает сравнение для заданного размера и типа данных."""
    import random
    
    if data_type == "random":
        data = list(range(size))
        random.shuffle(data)
        description = f"Случайный порядок ({size} элементов)"
    elif data_type == "reversed":
        data = list(range(size, 0, -1))
        description = f"Обратный порядок ({size} элементов)"
    elif data_type == "sorted":
        data = list(range(size))
        description = f"Уже отсортирован ({size} элементов)"
    elif data_type == "nearly_sorted":
        data = list(range(size))
        # Меняем местами несколько случайных элементов
        for _ in range(min(10, size // 10)):
            i = random.randint(0, size - 1)
            j = random.randint(0, size - 1)
            data[i], data[j] = data[j], data[i]
        description = f"Почти отсортирован ({size} элементов)"
    
    print(f"\n{'=' * 55}")
    print(f"  {description}")
    print(f"{'=' * 55}")
    
    algorithms = [
        ("Пузырьковая", bubble_sort_optimized),
        ("Выбором", selection_sort),
        ("Вставками", insertion_sort),
        ("sorted() [Timsort]", sorted),
    ]
    
    results = []
    
    for name, func in algorithms:
        elapsed, result = measure_time(func, data, name)
        results.append((name, elapsed))
    
    # Выводим результаты
    for name, elapsed in results:
        print(f"  {name:<25} {elapsed:>10.4f} мс")
    
    # Сравниваем с Timsort
    builtin_time = results[-1][1]
    print(f"\n  Относительно sorted():")
    for name, elapsed in results[:-1]:
        if builtin_time > 0:
            ratio = elapsed / builtin_time
            print(f"    {name:<25} в {ratio:>7.1f} раз медленнее")
    
    return results


# Запуск сравнения
print("=" * 55)
print("  СРАВНЕНИЕ АЛГОРИТМОВ СОРТИРОВКИ")
print("=" * 55)

sizes_and_types = [
    (500, "random"),
    (500, "reversed"),
    (500, "sorted"),
    (500, "nearly_sorted"),
]

all_results = {}

for size, data_type in sizes_and_types:
    results = run_comparison(size, data_type)
    all_results[data_type] = results

# Итоговая таблица
print(f"\n\n{'=' * 55}")
print("  ИТОГОВАЯ ТАБЛИЦА")
print(f"{'=' * 55}")
print()
print(f"{'Алгоритм':<20} {'Лучший':<12} {'Средний':<12} {'Худший':<12} {'Устойчивая?'}")
print("-" * 70)
print(f"{'Пузырьковая':<20} {'O(n)':<12} {'O(n²)':<12} {'O(n²)':<12} {'Да'}")
print(f"{'Выбором':<20} {'O(n²)':<12} {'O(n²)':<12} {'O(n²)':<12} {'Нет'}")
print(f"{'Вставками':<20} {'O(n)':<12} {'O(n²)':<12} {'O(n²)':<12} {'Да'}")
print(f"{'Timsort (sorted)':<20} {'O(n)':<12} {'O(n log n)':<12} {'O(n log n)':<12} {'Да'}")