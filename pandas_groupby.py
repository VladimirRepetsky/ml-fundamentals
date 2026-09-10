import pandas as pd
import numpy as np

df = pd.read_csv("data/students_with_gaps.csv")

# Предварительная очистка
df["age"] = df["age"].fillna(df["age"].median())
df["score"] = df["score"].fillna(df["score"].median())
df["hours_per_week"] = df["hours_per_week"].fillna(df["hours_per_week"].median())
df["gender"] = df["gender"].fillna(df["gender"].mode()[0])
df["course"] = df["course"].fillna(df["course"].mode()[0])

print("=== Исходные данные ===")
print(df.head())

# ============================================================
# 1. БАЗОВАЯ ГРУППИРОВКА
# ============================================================

print("\n=== 1. Базовая группировка ===")

# Средний балл по курсам
print("Средний балл по курсам:")
print(df.groupby("course")["score"].mean().round(2))

# Средний балл по полу
print("\nСредний балл по полу:")
print(df.groupby("gender")["score"].mean().round(2))

# Количество студентов по курсам
print("\nКоличество студентов по курсам:")
print(df.groupby("course").size())

# Или через count()
print("\nЧерез count():")
print(df.groupby("course")["student_id"].count())

# ============================================================
# 2. НЕСКОЛЬКО АГРЕГАЦИЙ
# ============================================================

print("\n=== 2. Несколько агрегаций ===")

# Несколько функций для одного столбца
print("Статистики балла по курсам:")
print(df.groupby("course")["score"].agg(["mean", "median", "min", "max", "count"]).round(2))

# Разные функции для разных столбцов
print("\nРазные агрегации:")
result = df.groupby("course").agg(
    avg_score=("score", "mean"),
    max_score=("score", "max"),
    avg_age=("age", "mean"),
    total_hours=("hours_per_week", "sum"),
    num_students=("student_id", "count")
).round(2)
print(result)

# ============================================================
# 3. ГРУППИРОВКА ПО НЕСКОЛЬКИМ СТОЛБЦАМ
# ============================================================

print("\n=== 3. Группировка по нескольким столбцам ===")

# Средний балл по курсу и полу
print("Средний балл по курсу и полу:")
result = df.groupby(["course", "gender"])["score"].mean().round(2)
print(result)

# Развёрнутый вид (unstack)
print("\nВ виде таблицы:")
print(result.unstack(fill_value=0).round(2))

# ============================================================
# 4. ОТВЕТЫ НА КОНКРЕТНЫЕ ВОПРОСЫ
# ============================================================

print("\n=== 4. Ответы на вопросы (как в задании программы) ===")

# Вопрос 1: Средний возраст студентов
avg_age = df["age"].mean()
print(f"Средний возраст студентов: {avg_age:.1f}")

# Вопрос 2: Количество студентов по полу
gender_counts = df.groupby("gender").size()
print(f"\nКоличество студентов по полу:")
print(gender_counts)

# Вопрос 3: Средний балл для разных курсов
course_scores = df.groupby("course")["score"].mean().round(2)
print(f"\nСредний балл по курсам:")
print(course_scores)

# Вопрос 4: Кто учится больше часов?
top_hours = df.nlargest(3, "hours_per_week")[["name", "hours_per_week", "course"]]
print(f"\nТоп-3 по часам обучения:")
print(top_hours)

# Вопрос 5: Какой курс самый эффективный?
df["efficiency"] = df["score"] / df["hours_per_week"]
course_efficiency = df.groupby("course")["efficiency"].mean().round(2)
print(f"\nЭффективность по курсам:")
print(course_efficiency.sort_values(ascending=False))

# ============================================================
# 5. TRANSFORM: добавление агрегатов обратно в DataFrame
# ============================================================

print("\n=== 5. Transform ===")

# Добавляем средний балл курса к каждой строке
df["course_avg_score"] = df.groupby("course")["score"].transform("mean")
print("Средний балл курса для каждого студента:")
print(df[["name", "course", "score", "course_avg_score"]].round(2))

# Отклонение от среднего по курсу
df["score_vs_course_avg"] = df["score"] - df["course_avg_score"]
print("\nОтклонение от среднего по курсу:")
print(df[["name", "course", "score", "score_vs_course_avg"]].round(2))