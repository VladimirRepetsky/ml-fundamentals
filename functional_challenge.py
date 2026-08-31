from functools import reduce

numbers = [12, -7, 5, 64, -1, 0, 33, 8]

squared = list(map(lambda x: x ** 2, numbers))
positive = list(filter(lambda x: x > 0, numbers))
negative = list(filter(lambda x: x < 0, numbers))
total = reduce(lambda acc, x: acc + x, numbers, 0)
product = reduce(lambda acc, x: acc * x, numbers, 1)

print("Исходные числа:", numbers)
print("Квадраты:", squared)
print("Положительные:", positive)
print("Отрицательные:", negative)
print("Сумма:", total)
print("Произведение:", product)

print("-" * 40)

prices = [100, 250, 40, 800, 60]

discounted_prices = list(map(lambda price: price * 0.9, prices))
expensive_prices = list(filter(lambda price: price >= 100, prices))
total_revenue = reduce(lambda acc, price: acc + price, prices, 0)

print("Исходные цены:", prices)
print("Цены со скидкой 10%:", discounted_prices)
print("Дорогие товары:", expensive_prices)
print("Общая сумма:", total_revenue)

print("-" * 40)

students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78),
    ("David", 88),
    ("Eve", 65)
]

sorted_by_score = sorted(
    students,
    key=lambda student: student[1],
    reverse=True
)

sorted_by_name = sorted(
    students,
    key=lambda student: student[0]
)

print("Студенты:")
print(students)

print("По баллу:")
print(sorted_by_score)

print("По имени:")
print(sorted_by_name)