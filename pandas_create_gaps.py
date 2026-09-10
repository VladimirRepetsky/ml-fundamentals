import pandas as pd
import numpy as np

# Данные о студентах с пропущенными значениями
students_data = {
    "student_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "name": ["Alice", "Bob", "Charlie", "David", "Eve",
             "Frank", "Grace", "Henry", "Ivy", "Jack"],
    "age": [22, 25, None, 30, 28, 24, None, 29, 21, 27],
    "gender": ["F", "M", "M", None, "F", "M", "F", "M", None, "M"],
    "course": ["Python", "ML", "Python", "ML", "Data Science",
               "Python", None, "Data Science", "Python", "ML"],
    "score": [85, 92, 78, None, 95, 72, 90, None, 68, 79],
    "hours_per_week": [10, 15, 8, 20, None, 6, 14, 18, 5, 10],
}

df = pd.DataFrame(students_data)
df.to_csv("data/students_with_gaps.csv", index=False)

print("Файл data/students_with_gaps.csv создан.")
print("\nСодержимое:")
print(df)
print("\nПропуски по столбцам:")
print(df.isnull().sum())