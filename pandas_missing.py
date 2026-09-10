import pandas as pd
import numpy as np

df = pd.read_csv("data/students_with_gaps.csv")

print("=== Исходные данные ===")
print(df)

# ============================================================
# 1. ОБНАРУЖЕНИЕ ПРОПУСКОВ
# ============================================================

print("\n=== 1. Обнаружение пропусков ===")

# Количество пропусков по каждому столбцу
print("Пропуски по столбцам:")
print(df.isnull().sum())

# Процент пропусков по каждому столбцу
print("\nПроцент пропусков:")
print((df.isnull().sum() / len(df) * 100).round(2))

# Общая информация о пропусках
print(f"\nВсего строк: {len(df)}")
print(f"Всего пропусков: {df.isnull().sum().sum()}")

# Строки с пропусками
print("\nСтроки, содержащие хотя бы один пропуск:")
rows_with_gaps = df[df.isnull().any(axis=1)]
print(rows_with_gaps)

# ============================================================
# 2. УДАЛЕНИЕ ПРОПУСКОВ
# ============================================================

print("\n=== 2. Удаление пропусков ===")

# Удалить все строки с пропусками
df_drop_all = df.dropna()
print(f"После dropna(): {len(df_drop_all)} строк (было {len(df)})")

# Удалить строки, где пропущен конкретный столбец
df_drop_score = df.dropna(subset=["score"])
print(f"После dropna(subset=['score']): {len(df_drop_score)} строк")

# Удалить строки, где пропущены ВСЕ значения
df_drop_all_cols = df.dropna(how="all")
print(f"После dropna(how='all'): {len(df_drop_all_cols)} строк")

# Удалить столбцы с пропусками
df_drop_cols = df.dropna(axis=1)
print(f"После dropna(axis=1): остались столбцы {df_drop_cols.columns.tolist()}")

# ============================================================
# 3. ЗАПОЛНЕНИЕ ПРОПУСКОВ
# ============================================================

print("\n=== 3. Заполнение пропусков ===")

# Заполнить одним значением
df_fill_zero = df.copy()
df_fill_zero["score"] = df_fill_zero["score"].fillna(0)
print("Заполнение score нулями:")
print(df_fill_zero[["name", "score"]])

# Заполнить средним значением
df_fill_mean = df.copy()
mean_age = df["age"].mean()
df_fill_mean["age"] = df_fill_mean["age"].fillna(mean_age)
print(f"\nЗаполнение age средним ({mean_age:.1f}):")
print(df_fill_mean[["name", "age"]])

# Заполнить медианой (устойчивее к выбросам)
df_fill_median = df.copy()
median_score = df["score"].median()
df_fill_median["score"] = df_fill_median["score"].fillna(median_score)
print(f"\nЗаполнение score медианой ({median_score}):")
print(df_fill_median[["name", "score"]])

# Заполнить модой (для категориальных данных)
df_fill_mode = df.copy()
mode_gender = df["gender"].mode()[0]
df_fill_mode["gender"] = df_fill_mode["gender"].fillna(mode_gender)
print(f"\nЗаполнение gender модой ('{mode_gender}'):")
print(df_fill_mode[["name", "gender"]])

# Заполнить предыдущим/следующим значением
df_fill_ffill = df.copy()
df_fill_ffill["course"] = df_fill_ffill["course"].ffill()
print("\nЗаполнение course предыдущим значением (ffill):")
print(df_fill_ffill[["name", "course"]])

# ============================================================
# 4. СТРАТЕГИЯ ОЧИСТКИ ДЛЯ РАЗНЫХ ТИПОВ ДАННЫХ
# ============================================================

print("\n=== 4. Стратегия очистки ===")
print("Числовые признаки → среднее или медиана")
print("Категориальные признаки → мода или отдельная категория 'Unknown'")
print("Целевая переменная → обычно удаляем строки (dropna)")
print("ID / ключи → проверяем вручную")

# Комплексная очистка
df_clean = df.copy()

# Числовые: заполняем медианой
numeric_cols = ["age", "score", "hours_per_week"]
for col in numeric_cols:
    df_clean[col] = df_clean[col].fillna(df_clean[col].median())

# Категориальные: заполняем модой или 'Unknown'
categorical_cols = ["gender", "course"]
for col in categorical_cols:
    mode_val = df_clean[col].mode()
    if len(mode_val) > 0:
        df_clean[col] = df_clean[col].fillna(mode_val[0])
    else:
        df_clean[col] = df_clean[col].fillna("Unknown")

print("\nОчищенный DataFrame:")
print(df_clean)
print("\nПропуски после очистки:")
print(df_clean.isnull().sum())