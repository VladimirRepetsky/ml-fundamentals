students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78),
    ("David", 88)
]

print("Исходный список:")
print(students)

sorted_by_score = sorted(students, key=lambda student: student[1])

print("\nОтсортировано по баллу по возрастанию:")
print(sorted_by_score)

sorted_by_score_desc = sorted(
    students,
    key=lambda student: student[1],
    reverse=True
)

print("\nОтсортировано по баллу по убыванию:")
print(sorted_by_score_desc)

sorted_by_name = sorted(students, key=lambda student: student[0])

print("\nОтсортировано по имени:")
print(sorted_by_name)

students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 85),
    ("David", 92)
]

sorted_students = sorted(
    students,
    key=lambda student: (student[1], student[0]),
    reverse=True
)

print("\nСортировка по баллу, затем по имени:")
print(sorted_students)

products = [
    {"name": "apple", "price": 120},
    {"name": "bread", "price": 80},
    {"name": "milk", "price": 150},
    {"name": "cheese", "price": 450}
]

sorted_products = sorted(products, key=lambda product: product["price"])

print("\nПродукты по цене:")

for product in sorted_products:
    print(f"{product['name']}: {product['price']}")

