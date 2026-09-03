import numpy as np
import time

# === Сравнение скорости: списки против NumPy ===

sizes = [10_000, 100_000, 1_000_000, 10_000_000]

print("=" * 60)
print("Сравнение скорости: списки против NumPy")
print("=" * 60)

for size in sizes:
    # Создаём данные
    python_list = list(range(size))
    numpy_array = np.arange(size)

    # --- Списки: умножение на 2 через цикл ---
    start = time.time()
    result_list = []
    for x in python_list:
        result_list.append(x * 2)
    time_list = (time.time() - start) * 1000

    # --- NumPy: векторное умножение ---
    start = time.time()
    result_numpy = numpy_array * 2
    time_numpy = (time.time() - start) * 1000

    speedup = time_list / time_numpy if time_numpy > 0 else float('inf')

    print(f"\nРазмер: {size:>12,}")
    print(f"  Список (цикл):  {time_list:>10.2f} мс")
    print(f"  NumPy (вектор): {time_numpy:>10.2f} мс")
    print(f"  Ускорение:      в {speedup:.1f} раз")

# === Сравнение скорости: сумма ===

print("\n" + "=" * 60)
print("Сравнение скорости: суммирование")
print("=" * 60)

size = 10_000_000
python_list = list(range(size))
numpy_array = np.arange(size)

# Сумма через цикл
start = time.time()
total = 0
for x in python_list:
    total += x
time_list = (time.time() - start) * 1000

# Сумма через sum()
start = time.time()
total = sum(python_list)
time_builtin = (time.time() - start) * 1000

# Сумма через np.sum()
start = time.time()
total = np.sum(numpy_array)
time_numpy = (time.time() - start) * 1000

print(f"\nРазмер: {size:,}")
print(f"  Цикл:       {time_list:>10.2f} мс")
print(f"  sum():      {time_builtin:>10.2f} мс")
print(f"  np.sum():   {time_numpy:>10.2f} мс")

# === Сравнение памяти ===

print("\n" + "=" * 60)
print("Сравнение памяти")
print("=" * 60)

size = 1_000_000

# Список из int
python_list = list(range(size))
# Примерный размер: каждый int в Python занимает ~28 байт
# Плюс указатель в списке ~8 байт
# Итого ~36 байт на элемент
approx_list_size = size * 36

# Массив из int64
numpy_array = np.arange(size, dtype=np.int64)
numpy_size = numpy_array.nbytes

print(f"\nРазмер: {size:,}")
print(f"  Список (примерно): {approx_list_size / 1_000_000:.1f} МБ")
print(f"  NumPy массив:      {numpy_size / 1_000_000:.1f} МБ")
print(f"  Экономия:          в {approx_list_size / numpy_size:.1f} раз")

print("\n" + "=" * 60)
print("Вывод: для числовых операций всегда используй NumPy.")
print("Это быстрее и расходует меньше памяти.")
print("=" * 60)