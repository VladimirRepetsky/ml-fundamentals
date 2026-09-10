import pandas as pd

df = pd.read_csv("data/students.csv")

print("Исходный DataFrame:")
print(df)

# === Фильтрация по одному условию ===

print("\n=== Студенты старше 25 лет ===")
older_students = df[df["age"] > 25]
print(older_students)

print("\n=== Студенты с баллом 85 и выше ===")
high_scores = df[df["score"] >= 85]
print(high_scores)

print("\n=== Студенты, которые прошли курс ===")
passed_students = df[df["passed"] == True]
print(passed_students)

# === Фильтрация по нескольким условиям ===

print("\n=== Студенты старше 25 И с баллом выше 80 ===")
result = df[(df["age"] > 25) & (df["score"] > 80)]
print(result)

print("\n=== Студенты младше 25 ИЛИ с баллом выше 90 ===")
result = df[(df["age"] < 25) | (df["score"] > 90)]
print(result)

print("\n=== Студенты НЕ из курса Python ===")
not_python = df[df["course"] != "Python"]
print(not_python)

# === Фильтрация с isin() ===

print("\n=== Студенты из курсов ML и Data Science ===")
result = df[df["course"].isin(["ML", "Data Science"])]
print(result)

# === Фильтрация по строковым значениям ===

print("\n=== Студенты, чьё имя начинается на 'A' ===")
result = df[df["name"].str.startswith("A")]
print(result)

print("\n=== Студенты, чьё имя содержит 'a' ===")
result = df[df["name"].str.contains("a", case=False)]
print(result)

# === Комбинированная фильтрация с выбором столбцов ===

print("\n=== Имена и баллы студентов старше 25 с баллом выше 80 ===")
result = df[(df["age"] > 25) & (df["score"] > 80)][["name", "score"]]
print(result)

# === Сортировка ===

print("\n=== Сортировка по баллу (по убыванию) ===")
sorted_df = df.sort_values("score", ascending=False)
print(sorted_df)

print("\n=== Сортировка по возрасту, затем по баллу ===")
sorted_df = df.sort_values(["age", "score"], ascending=[True, False])
print(sorted_df)

# === Топ-3 студента по баллу ===

print("\n=== Топ-3 студента по баллу ===")
top_3 = df.nlargest(3, "score")
print(top_3)

# === Последние 3 по баллу ===

print("\n=== Последние 3 по баллу ===")
bottom_3 = df.nsmallest(3, "score")
print(bottom_3)