import pandas as pd

# === Чтение CSV ===

df = pd.read_csv("data/students.csv")

print("=== DataFrame загружен ===")
print(df)

# === Первые и последние строки ===

print("\n=== Первые 5 строк ===")
print(df.head())

print("\n=== Первые 3 строки ===")
print(df.head(3))

print("\n=== Последние 5 строк ===")
print(df.tail())

# === Информация о DataFrame ===

print("\n=== Информация о DataFrame ===")
print("Форма:", df.shape)
print("Количество строк:", df.shape[0])
print("Количество столбцов:", df.shape[1])

print("\n=== Имена столбцов ===")
print(df.columns.tolist())

print("\n=== Типы данных ===")
print(df.dtypes)

# === Подробная информация: info() ===

print("\n=== info() ===")
df.info()

# === Статистика числовых столбцов: describe() ===

print("\n=== describe() ===")
print(df.describe())

print("\n=== describe() для нечисловых столбцов ===")
print(df.describe(include="object"))

# === Статистика для конкретного столбца ===

print("\n=== Статистика для столбца 'score' ===")
print("Среднее:", df["score"].mean())
print("Медиана:", df["score"].median())
print("Стандартное отклонение:", df["score"].std())
print("Минимум:", df["score"].min())
print("Максимум:", df["score"].max())
print("Количество:", df["score"].count())

# === Уникальные значения ===

print("\n=== Уникальные значения ===")
print("Уникальные курсы:", df["course"].unique())
print("Количество уникальных курсов:", df["course"].nunique())
print("Частота курсов:")
print(df["course"].value_counts())

print("\nУникальные полы:", df["gender"].unique())
print("Частота полов:")
print(df["gender"].value_counts())

# === Пропущенные значения ===

print("\n=== Пропущенные значения ===")
print(df.isnull().sum())