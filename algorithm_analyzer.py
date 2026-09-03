"""
Мини-проект: Анализатор производительности алгоритмов

Этот скрипт:
1. Реализует все изученные алгоритмы.
2. Тестирует их на разных типах данных.
3. Строит таблицу результатов.
4. Показывает, как время растёт с размером данных.
5. Визуализирует рост сложности (текстовый график).

Запуск:
    python algorithm_analyzer.py
"""
import time
import random


# ============================================================
# АЛГОРИТМЫ ПОИСКА
# ============================================================

def linear_search(data, target):
    """Линейный поиск — O(n)."""
    comparisons = 0
    for i in range(len(data)):
        comparisons += 1
        if data[i] == target:
            return i, comparisons
    return -1, comparisons


def binary_search(data, target):
    """Бинарный поиск — O(log n). Требует отсортированных данных."""
    left = 0
    right = len(data) - 1
    comparisons = 0
    
    while left <= right:
        comparisons += 1
        mid = (left + right) // 2
        
        if data[mid] == target:
            return mid, comparisons
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1, comparisons


# ============================================================
# АЛГОРИТМЫ СОРТИРОВКИ
# ============================================================

def bubble_sort(data):
    """Пузырьковая сортировка с оптимизацией."""
    data = data.copy()
    n = len(data)
    comparisons = 0
    swaps = 0
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparisons += 1
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swaps += 1
                swapped = True
        if not swapped:
            break
    
    return data, comparisons, swaps


def selection_sort(data):
    """Сортировка выбором."""
    data = data.copy()
    n = len(data)
    comparisons = 0
    swaps = 0
    
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            comparisons += 1
            if data[j] < data[min_index]:
                min_index = j
        if min_index != i:
            data[i], data[min_index] = data[min_index], data[i]
            swaps += 1
    
    return data, comparisons, swaps


def insertion_sort(data):
    """Сортировка вставками."""
    data = data.copy()
    n = len(data)
    comparisons = 0
    shifts = 0
    
    for i in range(1, n):
        key = data[i]
        j = i - 1
        
        while j >= 0 and data[j] > key:
            comparisons += 1
            data[j + 1] = data[j]
            j -= 1
            shifts += 1
        
        if j >= 0:
            comparisons += 1
        
        data[j + 1] = key
    
    return data, comparisons, shifts


# ============================================================
# УТИЛИТЫ ДЛЯ ТЕСТИРОВАНИЯ
# ============================================================

def generate_data(size, data_type="random"):
    """Генерирует тестовые данные."""
    if data_type == "random":
        data = list(range(size))
        random.shuffle(data)
    elif data_type == "reversed":
        data = list(range(size, 0, -1))
    elif data_type == "sorted":
        data = list(range(size))
    elif data_type == "nearly_sorted":
        data = list(range(size))
        num_swaps = max(1, size // 20)
        for _ in range(num_swaps):
            i = random.randint(0, size - 1)
            j = random.randint(0, size - 1)
            data[i], data[j] = data[j], data[i]
    else:
        data = list(range(size))
        random.shuffle(data)
    
    return data


def measure_sort(func, data):
    """Измеряет время и характеристики сортировки."""
    start = time.time()
    result, comparisons, swaps = func(data)
    elapsed = (time.time() - start) * 1000
    return elapsed, comparisons, swaps, result


def text_bar(value, max_value, width=30):
    """Рисует текстовую полосу для визуализации."""
    if max_value == 0:
        return ""
    bar_length = int((value / max_value) * width)
    return "█" * bar_length


# ============================================================
# ОСНОВНАЯ ПРОГРАММА
# ============================================================

def analyze_search():
    """Анализ алгоритмов поиска."""
    print("\n" + "=" * 60)
    print("  ЧАСТЬ 1: АНАЛИЗ АЛГОРИТМОВ ПОИСКА")
    print("=" * 60)
    
    sizes = [100, 1_000, 10_000, 100_000]
    
    print(f"\n{'Размер':<10} {'Линейный (шаги)':<20} {'Бинарный (шаги)':<20} {'Выигрыш'}")
    print("-" * 65)
    
    for size in sizes:
        data = list(range(size))
        target = size - 1  # Ищем последний элемент (худший случай)
        
        _, linear_steps = linear_search(data, target)
        _, binary_steps = binary_search(data, target)
        
        advantage = linear_steps / binary_steps if binary_steps > 0 else 0
        
        print(f"{size:<10} {linear_steps:<20} {binary_steps:<20} в {advantage:.0f} раз")
    
    print(f"\nВывод: бинарный поиск O(log n) против линейного O(n).")
    print(f"На {sizes[-1]} элементов бинарный поиск делает ~{20} шагов")
    print(f"вместо {sizes[-1]} у линейного.")


def analyze_sorts():
    """Анализ алгоритмов сортировки."""
    print("\n" + "=" * 60)
    print("  ЧАСТЬ 2: АНАЛИЗ АЛГОРИТМОВ СОРТИРОВКИ")
    print("=" * 60)
    
    size = 1000
    data_types = ["random", "reversed", "sorted", "nearly_sorted"]
    data_type_names = {
        "random": "Случайный порядок",
        "reversed": "Обратный порядок",
        "sorted": "Уже отсортирован",
        "nearly_sorted": "Почти отсортирован",
    }
    
    algorithms = [
        ("Пузырьковая", bubble_sort),
        ("Выбором", selection_sort),
        ("Вставками", insertion_sort),
    ]
    
    for data_type in data_types:
        data = generate_data(size, data_type)
        
        print(f"\n  {data_type_names[data_type]} ({size} элементов):")
        print(f"  {'Алгоритм':<18} {'Время (мс)':<14} {'Сравнения':<14} {'Обмены':<10}")
        print(f"  {'-' * 56}")
        
        times = []
        
        for name, func in algorithms:
            elapsed, comps, swaps, _ = measure_sort(func, data)
            times.append(elapsed)
            print(f"  {name:<18} {elapsed:<14.3f} {comps:<14} {swaps:<10}")
        
        # Встроенная сортировка для сравнения
        start = time.time()
        sorted(data)
        builtin_time = (time.time() - start) * 1000
        print(f"  {'sorted()':<18} {builtin_time:<14.6f} {'—':<14} {'—':<10}")
        
        print(f"\n  Визуализация времени:")
        max_time = max(times) if times else 1
        for (name, _), elapsed in zip(algorithms, times):
            bar = text_bar(elapsed, max_time)
            print(f"    {name:<18} |{bar} {elapsed:.3f} мс")


def analyze_scaling():
    """Анализ роста времени с увеличением размера данных."""
    print("\n" + "=" * 60)
    print("  ЧАСТЬ 3: РОСТ ВРЕМЕНИ С УВЕЛИЧЕНИЕМ РАЗМЕРА")
    print("=" * 60)
    
    sizes = [100, 200, 400, 800, 1600]
    
    print(f"\n{'Размер':<10} {'Пузырьковая':<16} {'Выбором':<16} {'Вставками':<16}")
    print("-" * 58)
    
    for size in sizes:
        data = generate_data(size, "random")
        
        t1, _, _, _ = measure_sort(bubble_sort, data)
        t2, _, _, _ = measure_sort(selection_sort, data)
        t3, _, _, _ = measure_sort(insertion_sort, data)
        
        print(f"{size:<10} {t1:<16.3f} {t2:<16.3f} {t3:<16.3f}")
    
    print(f"\nПри увеличении размера в 2 раза время растёт в ~4 раза.")
    print(f"Это и есть O(n²) в действии.")
    
    # Показываем квадратичный рост
    print(f"\n  Проверка квадратичности:")
    data_small = generate_data(200, "random")
    data_large = generate_data(400, "random")
    
    t_small, _, _, _ = measure_sort(insertion_sort, data_small)
    t_large, _, _, _ = measure_sort(insertion_sort, data_large)
    
    ratio = t_large / t_small if t_small > 0 else 0
    print(f"  Размер 200 → {t_small:.3f} мс")
    print(f"  Размер 400 → {t_large:.3f} мс")
    print(f"  Отношение: {ratio:.1f} (ожидается ~4.0 для O(n²))")


def final_summary():
    """Итоговая сводка блока."""
    print("\n" + "=" * 60)
    print("  ИТОГОВАЯ СВОДКА БЛОКА ДЕНЬ 11–12")
    print("=" * 60)
    
    print("""
    ┌─────────────────────────────────────────────────────────┐
    │ АЛГОРИТМЫ ПОИСКА                                        │
    ├─────────────────────┬────────────┬──────────────────────┤
    │ Алгоритм            │ Сложность  │ Требует сортировки?  │
    ├─────────────────────┼────────────┼──────────────────────┤
    │ Линейный поиск      │ O(n)       │ Нет                  │
    │ Бинарный поиск      │ O(log n)   │ Да                   │
    └─────────────────────┴────────────┴──────────────────────┘
    
    ┌─────────────────────────────────────────────────────────────────┐
    │ АЛГОРИТМЫ СОРТИРОВКИ                                            │
    ├───────────────┬──────────┬──────────┬──────────┬────────────────┤
    │ Алгоритм      │ Лучший   │ Средний  │ Худший   │ Устойчивость   │
    ├───────────────┼──────────┼──────────┼──────────┼────────────────┤
    │ Пузырьковая   │ O(n)     │ O(n²)    │ O(n²)    │ ✅ Устойчивая  │
    │ Выбором       │ O(n²)    │ O(n²)    │ O(n²)    │ ❌ Неустойчива │
    │ Вставками     │ O(n)     │ O(n²)    │ O(n²)    │ ✅ Устойчивая  │
    │ Timsort       │ O(n)     │ O(n log n)│ O(n log n)│ ✅ Устойчивая│
    └───────────────┴──────────┴──────────┴──────────┴────────────────┘
    
    КЛЮЧЕВЫЕ ВЫВОДЫ:
    
    1. Для поиска: если данные отсортированы → бинарный поиск.
       Иначе → линейный поиск или множество (set) для O(1).
    
    2. Для сортировки в продакшене: всегда используй sorted().
       Простые сортировки нужны для понимания и собеседований.
    
    3. Сортировка вставками лучше пузырьковой и выбором для
       почти отсортированных данных и маленьких массивов.
    
    4. Big O помогает предсказать производительность:
       - 1 000 элементов: разница незаметна
       - 1 000 000 элементов: разница в ТЫСЯЧИ раз
    
    5. Устойчивость важна при многоступенчатой сортировке.
    """)


# ============================================================
# ЗАПУСК
# ============================================================

if __name__ == "__main__":
    print("\n" + "█" * 60)
    print("  АНАЛИЗАТОР ПРОИЗВОДИТЕЛЬНОСТИ АЛГОРИТМОВ")
    print("  День 12: Введение в алгоритмы — поиск и сортировка")
    print("█" * 60)
    
    analyze_search()
    analyze_sorts()
    analyze_scaling()
    final_summary()
    
    print("\n" + "=" * 60)
    print("  Блок День 11–12 завершён! 🎉")
    print("=" * 60 + "\n")