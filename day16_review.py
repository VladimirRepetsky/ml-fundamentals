import pandas as pd

df = pd.read_csv("data/students.csv")

print("=== Повторение Дня 15 ===")
print("Форма:", df.shape)
print("\nПервые 3 строки:")
print(df.head(3))

print("\nТипы данных:")
print(df.dtypes)

print("\nСтатистика:")
print(df.describe())

print("\nФильтрация (score > 85):")
print(df[df["score"] > 85][["name", "score"]])

print("\nВыбор столбцов:")
print(df[["name", "course", "score"]].head(3))

print("\nВсё работает — идём дальше.")