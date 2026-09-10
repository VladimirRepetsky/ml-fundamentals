import pandas as pd

# === Создание CSV файла с данными о студентах ===

students_data = {
    "student_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "name": [
        "Alice", "Bob", "Charlie", "David", "Eve",
        "Frank", "Grace", "Henry", "Ivy", "Jack"
    ],
    "age": [22, 25, 23, 30, 28, 24, 26, 29, 21, 27],
    "gender": ["F", "M", "M", "M", "F", "M", "F", "M", "F", "M"],
    "course": [
        "Python", "ML", "Python", "ML", "Data Science",
        "Python", "ML", "Data Science", "Python", "ML"
    ],
    "score": [85, 92, 78, 88, 95, 72, 90, 83, 68, 79],
    "hours_per_week": [10, 15, 8, 20, 12, 6, 14, 18, 5, 10],
    "passed": [True, True, False, True, True, False, True, True, False, True],
}

df = pd.DataFrame(students_data)

# Сохраняем в CSV
df.to_csv("data/students.csv", index=False)

print("Файл data/students.csv создан.")
print("\nСодержимое:")
print(df)