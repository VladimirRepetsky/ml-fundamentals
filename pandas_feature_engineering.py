import pandas as pd
import numpy as np

df = pd.read_csv("data/students_with_gaps.csv")

# Предварительная очистка
df["age"] = df["age"].fillna(df["age"].median())
df["score"] = df["score"].fillna(df["score"].median())
df["hours_per_week"] = df["hours_per_week"].fillna(df["hours_per_week"].median())
df["gender"] = df["gender"].fillna(df["gender"].mode()[0])
df["course"] = df["course"].fillna(df["course"].mode()[0])

print("=== Исходные данные (очищенные) ===")
print(df.head())

# ============================================================
# 1. АРИФМЕТИЧЕСКИЕ ПРИЗНАКИ
# ============================================================

print("\n=== 1. Арифметические признаки ===")

# Эффективность обучения
df["efficiency"] = df["score"] / df["hours_per_week"]
print("Эффективность (score / hours):")
print(df[["name", "score", "hours_per_week", "efficiency"]].round(2))

# Нормализованный балл (0-1)
df["score_normalized"] = (df["score"] - df["score"].min()) / \
                         (df["score"].max() - df["score"].min())
print("\nНормализованный балл:")
print(df[["name", "score", "score_normalized"]].round(3))

# Стандартизированный возраст
df["age_standardized"] = (df["age"] - df["age"].mean()) / df["age"].std()
print("\nСтандартизированный возраст:")
print(df[["name", "age", "age_standardized"]].round(3))

# ============================================================
# 2. КАТЕГОРИАЛЬНЫЕ ПРИЗНАКИ
# ============================================================

print("\n=== 2. Категориальные признаки ===")

# Возрастная категория
df["age_category"] = pd.cut(
    df["age"],
    bins=[0, 23, 26, 30, 100],
    labels=["young", "mid_young", "mid_senior", "senior"]
)
print("Возрастные категории:")
print(df[["name", "age", "age_category"]])

# Уровень успеваемости
df["grade"] = pd.cut(
    df["score"],
    bins=[0, 60, 70, 80, 90, 100],
    labels=["F", "D", "C", "B", "A"]
)
print("\nУровень успеваемости:")
print(df[["name", "score", "grade"]])

# Интенсивность обучения
df["intensity"] = pd.cut(
    df["hours_per_week"],
    bins=[0, 8, 15, 100],
    labels=["low", "medium", "high"]
)
print("\nИнтенсивность обучения:")
print(df[["name", "hours_per_week", "intensity"]])

# ============================================================
# 3. УСЛОВНЫЕ ПРИЗНАКИ
# ============================================================

print("\n=== 3. Условные признаки ===")

# Флаг высокого балла
df["is_high_scorer"] = (df["score"] >= 85).astype(int)
print("Флаг высокого балла (>= 85):")
print(df[["name", "score", "is_high_scorer"]])

# Флаг интенсивного обучения
df["is_intensive"] = np.where(df["hours_per_week"] >= 15, 1, 0)
print("\nФлаг интенсивного обучения (>= 15 ч/нед):")
print(df[["name", "hours_per_week", "is_intensive"]])

# Комбинированный признак
df["top_student"] = ((df["score"] >= 85) & (df["hours_per_week"] >= 10)).astype(int)
print("\nТоп-студент (высокий балл + интенсивное обучение):")
print(df[["name", "score", "hours_per_week", "top_student"]])

# ============================================================
# 4. ТЕКСТОВЫЕ ПРИЗНАКИ
# ============================================================

print("\n=== 4. Текстовые признаки ===")

# Длина имени
df["name_length"] = df["name"].str.len()
print("Длина имени:")
print(df[["name", "name_length"]])

# Первая буква имени
df["first_letter"] = df["name"].str[0]
print("\nПервая буква имени:")
print(df[["name", "first_letter"]])

# ============================================================
# ИТОГО
# ============================================================

print("\n=== Итоговый DataFrame с новыми признаками ===")
print(df.columns.tolist())
print(f"\nБыло столбцов: 7, стало: {len(df.columns)}")
print(f"Новые признаки: {len(df.columns) - 7}")