import time


# O(1) — константное время
def get_first_element(data):
    """Всегда одна операция, независимо от размера."""
    return data[0] if data else None


# O(n) — линейное время
def find_max_linear(data):
    """Проходим по каждому элементу один раз."""
    if not data:
        return None
    maximum = data[0]
    for item in data:
        if item > maximum:
            maximum = item
    return maximum


# O(n²) — квадратичное время
def has_duplicates_quadratic(data):
    """Сравниваем каждый элемент с каждым."""
    n = len(data)
    for i in range(n):
        for j in range(i + 1, n):
            if data[i] == data[j]:
                return True
    return False


# O(n) — линейное время (оптимизированная версия)
def has_duplicates_linear(data):
    """Используем множество для проверки за O(n)."""
    seen = set()
    for item in data:
        if item in seen:
            return True
        seen.add(item)
    return False


def measure_time(func, data, label):
    """Измеряет время выполнения функции."""
    start = time.time()
    result = func(data)
    end = time.time()
    elapsed = (end - start) * 1000  # миллисекунды
    print(f"{label}: {elapsed:.4f} мс (размер данных: {len(data)})")
    return result


# Тестирование
sizes = [100, 1_000, 10_000, 100_000]

print("=" * 60)
print("Демонстрация Big O на практике")
print("=" * 60)

for size in sizes:
    data = list(range(size))
    print(f"\n--- Размер данных: {size} ---")
    measure_time(get_first_element, data, "O(1) get_first_element")
    measure_time(find_max_linear, data, "O(n) find_max_linear")

print("\n" + "=" * 60)
print("Сравнение O(n²) и O(n) для поиска дубликатов")
print("=" * 60)

# Для O(n²) берём маленькие размеры, иначе будет очень долго
small_sizes = [100, 500, 1_000, 2_000]

for size in small_sizes:
    data = list(range(size)) + [size // 2]  # добавляем один дубликат
    print(f"\n--- Размер данных: {size} ---")
    measure_time(has_duplicates_quadratic, data, "O(n²) has_duplicates_quadratic")
    measure_time(has_duplicates_linear, data, "O(n)  has_duplicates_linear")