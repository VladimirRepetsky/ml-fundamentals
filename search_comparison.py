"""
Сравнение алгоритмов поиска и сортировки.
Демонстрация разницы в производительности.
"""
import time
from linear_search import linear_search
from binary_search import binary_search
from bubble_sort import bubble_sort_optimized
from selection_sort import selection_sort


def measure(func, *args):
    """Измеряет время выполнения в миллисекундах."""
    start = time.time()
    result = func(*args)
    elapsed = (time.time() - start) * 1000
    return result, elapsed


print("=" * 60)
print("СРАВНЕНИЕ АЛГОРИТМОВ")
print("=" * 60)

# === Сравнение поиска ===
print("\n--- Поиск в массиве из 100 000 элементов ---")

data = list(range(1, 100_001))
target = 99_999

# Линейный поиск
_, linear_time = measure(linear_search, data, target)

# Бинарный поиск
_, binary_time = measure(binary_search, data, target)

print(f"Линейный поиск:  {linear_time:.4f} мс")
print(f"Бинарный поиск:  {binary_time:.6f} мс")
print(f"Бинарный быстрее в {linear_time / binary_time:.0f} раз")

# === Сравнение сортировок ===
print("\n--- Сортировка массива из 2000 элементов (обратный порядок) ---")

data = list(range(2000, 0, -1))

_, bubble_time = measure(bubble_sort_optimized, data.copy())
_, selection_time = measure(selection_sort, data.copy())

print(f"Пузырьковая:     {bubble_time:.2f} мс")
print(f"Выбором:         {selection_time:.2f} мс")

# === Сравнение с встроенной сортировкой Python ===
print("\n--- Сравнение с встроенной sorted() ---")

data = list(range(2000, 0, -1))

_, builtin_time = measure(sorted, data)

print(f"sorted() (Timsort): {builtin_time:.4f} мс")
print(f"Пузырьковая:        {bubble_time:.2f} мс")
print(f"Выбором:            {selection_time:.2f} мс")
print()
print(f"sorted() быстрее пузырьковой в {bubble_time / builtin_time:.0f} раз")
print(f"sorted() быстрее выбором в {selection_time / builtin_time:.0f} раз")

# === Итоговая таблица ===
print("\n" + "=" * 60)
print("ИТОГОВАЯ ТАБЛИЦА СЛОЖНОСТИ")
print("=" * 60)
print()
print(f"{'Алгоритм':<30} {'Лучший':<12} {'Средний':<12} {'Худший':<12}")
print("-" * 66)
print(f"{'Линейный поиск':<30} {'O(n)':<12} {'O(n)':<12} {'O(n)':<12}")
print(f"{'Бинарный поиск':<30} {'O(1)':<12} {'O(log n)':<12} {'O(log n)':<12}")
print(f"{'Пузырьковая сортировка':<30} {'O(n)':<12} {'O(n²)':<12} {'O(n²)':<12}")
print(f"{'Сортировка выбором':<30} {'O(n²)':<12} {'O(n²)':<12} {'O(n²)':<12}")
print(f"{'sorted() / Timsort':<30} {'O(n)':<12} {'O(n log n)':<12} {'O(n log n)':<12}")