import numpy as np

# === Арифметические операции ===

a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])

print("a =", a)
print("b =", b)

print("\n=== Арифметика (поэлементно) ===")
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a ** 2 =", a ** 2)
print("a % 3 =", a % 3)

# === Операция со скаляром ===

print("\n=== Операция со скаляром ===")
print("a + 10 =", a + 10)
print("a * 3 =", a * 3)
print("a - 5 =", a - 5)
print("a / 2 =", a / 2)

# === Математические функции ===

print("\n=== Математические функции ===")
print("np.sqrt(a) =", np.sqrt(a))
print("np.abs(a) =", np.abs(np.array([-1, -2, 3])))
print("np.sin(a) =", np.sin(a))
print("np.cos(a) =", np.cos(a))
print("np.exp(a) =", np.exp(np.array([0, 1, 2])))
print("np.log(a) =", np.log(a))
print("np.round([1.456, 2.789, 3.123], 2) =", np.round([1.456, 2.789, 3.123], 2))

# === Агрегатные функции ===

data = np.array([12, -7, 5, 64, -1, 0, 33, 8])

print("\n=== Агрегатные функции ===")
print("Массив:", data)
print("np.sum:", np.sum(data))
print("np.mean:", np.mean(data))
print("np.max:", np.max(data))
print("np.min:", np.min(data))
print("np.std:", np.std(data))       # стандартное отклонение
print("np.var:", np.var(data))       # дисперсия
print("np.median:", np.median(data))
print("np.argmin:", np.argmin(data))  # индекс минимума
print("np.argmax:", np.argmax(data))  # индекс максимума

# === Сравнение со списками ===
# Раньше ты писал:
# total = 0
# for number in numbers:
#     total += number

# Теперь:
# total = np.sum(numbers)

print("\n=== Сравнение подходов ===")
print("Сумма через np.sum:", np.sum(data))
print("Среднее через np.mean:", np.mean(data))
print("Максимум через np.max:", np.max(data))