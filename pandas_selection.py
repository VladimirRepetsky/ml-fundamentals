import pandas as pd

df = pd.read_csv("data/students.csv")

print("Исходный DataFrame:")
print(df)

# === Выбор одного столбца ===

print("\n=== Выбор одного столбца ===")
names = df["name"]
print(names)
print("Тип:", type(names))

# === Выбор нескольких столбцов ===

print("\n=== Выбор нескольких столбцов ===")
subset = df[["name", "age", "score"]]
print(subset)
print("Тип:", type(subset))

# === Выбор строки по индексу через .loc ===

print("\n=== .loc (по метке) ===")
print("Строка с индексом 0:")
print(df.loc[0])

print("\nСтроки с индексами 0, 2, 4:")
print(df.loc[[0, 2, 4]])

print("\nСтроки с 0 по 3 (включительно):")
print(df.loc[0:3])

# === Выбор строки по позиции через .iloc ===

print("\n=== .iloc (по позиции) ===")
print("Первая строка:")
print(df.iloc[0])

print("\nПервые 3 строки:")
print(df.iloc[:3])

print("\nПоследние 2 строки:")
print(df.iloc[-2:])

# === Выбор конкретных ячеек ===

print("\n=== Выбор конкретных ячеек ===")
print("Ячейка [0, 'name']:", df.loc[0, "name"])
print("Ячейка [0, 1]:", df.iloc[0, 1])

print("\nПодматрица:")
print(df.loc[0:3, ["name", "age", "score"]])

# === Разница между .loc и .iloc ===

print("\n=== Разница между .loc и .iloc ===")
print("df.loc[0:3] включает строку 3:")
print(df.loc[0:3])
print("\ndf.iloc[0:3] НЕ включает строку 3:")
print(df.iloc[0:3])

# === Доступ к значениям ===

print("\n=== Доступ к значениям ===")
print("Возраст Alice:", df.loc[df["name"] == "Alice", "age"].values[0])
print("Балл Bob:", df.loc[df["name"] == "Bob", "score"].values[0])