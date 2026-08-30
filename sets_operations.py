python_students = {"Alice", "Bob", "Charlie", "David"}
ml_students = {"Charlie", "Eve", "Frank", "Alice"}

# Пересечение: кто изучает и Python, и ML
both = python_students.intersection(ml_students)
print("Изучают и Python, и ML:", both)

# Объединение: все студенты
all_students = python_students.union(ml_students)
print("Все студенты:", all_students)

# Разница: кто изучает Python, но не изучает ML
only_python = python_students.difference(ml_students)
print("Только Python:", only_python)

# Симметрическая разница: кто изучает только что-то одно
only_one = python_students.symmetric_difference(ml_students)
print("Только один из курсов:", only_one)

