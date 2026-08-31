from functools import reduce

students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78),
    ("David", 88),
    ("Eve", 65)
]

# Средний балл
total_score = reduce(lambda acc, student: acc + student[1], students, 0)
average_score = total_score / len(students)

print("Средний балл:", round(average_score, 2))

# Студенты с баллом 80 и выше
good_students = list(filter(lambda student: student[1] >= 80, students))

print("\nСтуденты с баллом 80 и выше:")

for student in good_students:
    print(student)

# Имена всех студентов
names = list(map(lambda student: student[0], students))

print("\nИмена студентов:")
print(names)

# Лучший студент
best_student = max(students, key=lambda student: student[1])

print("\nЛучший студент:")
print(best_student)

# Сортировка по баллу
sorted_students = sorted(
    students,
    key=lambda student: student[1],
    reverse=True
)

print("\nСтуденты по баллу:")
print(sorted_students)