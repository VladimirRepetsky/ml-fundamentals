import numpy as np

# === Скалярное произведение векторов ===
# Алгебраическое определение:
# dot(a, b) = a[0]*b[0] + a[1]*b[1] + ... + a[n]*b[n]

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("=== Скалярное произведение ===")
print("a =", a)
print("b =", b)

# Способ 1: вручную
manual = a[0]*b[0] + a[1]*b[1] + a[2]*b[2]
print(f"\nВручную: {a[0]}*{b[0]} + {a[1]}*{b[1]} + {a[2]}*{b[2]} = {manual}")

# Способ 2: цикл
loop_result = 0
for i in range(len(a)):
    loop_result += a[i] * b[i]
print(f"Через цикл: {loop_result}")

# Способ 3: векторное умножение + сумма
vectorized = np.sum(a * b)
print(f"Через np.sum(a * b): {vectorized}")

# Способ 4: встроенная функция
builtin = np.dot(a, b)
print(f"Через np.dot(a, b): {builtin}")

# Способ 5: оператор @
operator = a @ b
print(f"Через a @ b: {operator}")

# === Проверка: все способы дают один результат ===
print(f"\nВсе способы дают {manual}: {manual == loop_result == vectorized == builtin == operator}")

# === Пример из жизни: стоимость корзины ===
print("\n=== Пример: стоимость корзины ===")
prices = np.array([120, 80, 150])      # цены товаров
quantities = np.array([3, 2, 1])        # количества

total_cost = np.dot(prices, quantities)
print(f"Цены: {prices}")
print(f"Количества: {quantities}")
print(f"Итого: {total_cost} руб.")
# 120*3 + 80*2 + 150*1 = 360 + 160 + 150 = 670