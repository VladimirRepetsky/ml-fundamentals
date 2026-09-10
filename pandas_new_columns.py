import pandas as pd

df = pd.read_csv("data/students.csv")

print("Исходный DataFrame:")
print(df.head())

# === Создание нового столбца ===

# Столбец с оценкой на основе балла
df["grade"] = df["score"].apply(
    lambda x: "A" if x >= 90 else
              "B" if x >= 80 else
              "C" if x >= 70 else
              "D" if x >= 60 else
              "F"
)

print("\n=== Добавлен столбец 'grade' ===")
print(df[["name", "score", "grade"]])

# === Создание столбца на основе других столбцов ===

# Эффективность: балл за час обучения
df["efficiency"] = df["score"] / df["hours_per_week"]

print("\n=== Добавлен столбец 'efficiency' ===")
print(df[["name", "score", "hours_per_week", "efficiency"]].round(2))

# === Создание столбца через np.where ===

import numpy as np

df["is_senior"] = np.where(df["age"] >= 25, "senior", "junior")

print("\n=== Добавлен столбец 'is_senior' ===")
print(df[["name", "age", "is_senior"]])

# === Создание столбца через условия ===

df["category"] = "average"
df.loc[df["score"] >= 90, "category"] = "excellent"
df.loc[df["score"] < 70, "category"] = "needs_improvement"

print("\n=== Добавлен столбец 'category' ===")
print(df[["name", "score", "category"]])

# === Удаление столбца ===

print("\n=== Удаление столбца ===")
df_copy = df.copy()
df_copy = df_copy.drop("efficiency", axis=1)
print("После удаления 'efficiency':")
print(df_copy.columns.tolist())

# === Сохранение изменённого DataFrame ===

df.to_csv("data/students_enriched.csv", index=False)
print("\nСохранено в data/students_enriched.csv")