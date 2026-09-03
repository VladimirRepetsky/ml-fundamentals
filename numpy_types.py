import numpy as np

# === Типы данных в NumPy ===

# int — целые числа
int_arr = np.array([1, 2, 3, 4, 5])
print("int массив:", int_arr, "dtype:", int_arr.dtype)

# float — дробные числа
float_arr = np.array([1.0, 2.5, 3.7])
print("float массив:", float_arr, "dtype:", float_arr.dtype)

# bool — булевы значения
bool_arr = np.array([True, False, True, False])
print("bool массив:", bool_arr, "dtype:", bool_arr.dtype)

# str — строки (редко используется в ML)
str_arr = np.array(["hello", "world"])
print("str массив:", str_arr, "dtype:", str_arr.dtype)

# === Явное указание типа ===

# Массив целых, но храним как float
float_from_int = np.array([1, 2, 3], dtype=np.float64)
print("\nint как float:", float_from_int, "dtype:", float_from_int.dtype)

# Массив дробных, но храним как int (дробная часть отбрасывается)
int_from_float = np.array([1.7, 2.9, 3.2], dtype=np.int32)
print("float как int:", int_from_float, "dtype:", int_from_float.dtype)

# === Преобразование типов ===

arr = np.array([1, 2, 3, 4, 5])
print("\nИсходный:", arr, "dtype:", arr.dtype)

# Преобразуем в float
arr_float = arr.astype(np.float64)
print("После astype(float):", arr_float, "dtype:", arr_float.dtype)

# Преобразуем в bool
arr_bool = arr.astype(bool)
print("После astype(bool):", arr_bool, "dtype:", arr_bool.dtype)

# === Важные типы данных ===
print("\n=== Основные типы данных NumPy ===")
print("np.int32 — целое, 4 байта")
print("np.int64 — целое, 8 байт")
print("np.float32 — дробное, 4 байта")
print("np.float64 — дробное, 8 байт")
print("np.bool_ — булево, 1 байт")

# === Размер в памяти ===
arr_int32 = np.array([1, 2, 3, 4, 5], dtype=np.int32)
arr_int64 = np.array([1, 2, 3, 4, 5], dtype=np.int64)
arr_float32 = np.array([1, 2, 3, 4, 5], dtype=np.float32)
arr_float64 = np.array([1, 2, 3, 4, 5], dtype=np.float64)

print(f"\nint32:  {arr_int32.nbytes} байт")
print(f"int64:  {arr_int64.nbytes} байт")
print(f"float32: {arr_float32.nbytes} байт")
print(f"float64: {arr_float64.nbytes} байт")