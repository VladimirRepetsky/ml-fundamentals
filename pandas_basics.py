import pandas as pd
import numpy as np

# === Создание Series ===

# Из списка
numbers = pd.Series([10, 20, 30, 40, 50])
print("Series из списка:")
print(numbers)
print("Тип:", type(numbers))

# Из списка с индексами
fruits = pd.Series(
    ["apple", "banana", "cherry"],
    index=["a", "b", "c"]
)
print("\nSeries с индексами:")
print(fruits)

# Из словаря
ages = pd.Series({
    "Alice": 25,
    "Bob": 30,
    "Charlie": 35
})
print("\nSeries из словаря:")
print(ages)

# === Свойства Series ===

print("\n=== Свойства Series ===")
print("Значения:", numbers.values)
print("Индексы:", numbers.index)
print("Длина:", len(numbers))
print("Тип данных:", numbers.dtype)

# === Доступ к элементам ===

print("\n=== Доступ к элементам ===")
print("Первый элемент:", numbers[0])
print("Последний элемент:", numbers[-1])
print("По индексу 'a':", fruits["a"])
print("Срез:", numbers[1:4])

# === Векторные операции ===

print("\n=== Векторные операции ===")
print("Умножение на 2:")
print(numbers * 2)

print("\nСложение:")
print(numbers + 10)

print("\nСреднее:", numbers.mean())
print("Сумма:", numbers.sum())
print("Максимум:", numbers.max())
print("Минимум:", numbers.min())

# === Булева индексация ===

print("\n=== Булева индексация ===")
print("Элементы больше 25:")
print(numbers[numbers > 25])


# === Создание DataFrame ===

# Из словаря списков
data = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [25, 30, 35, 28],
    "city": ["Moscow", "Berlin", "London", "Paris"],
    "score": [85, 92, 78, 88]
}

df = pd.DataFrame(data)

print("\n=== DataFrame из словаря ===")
print(df)
print("\nТип:", type(df))

# === Свойства DataFrame ===

print("\n=== Свойства DataFrame ===")
print("Форма:", df.shape)
print("Количество строк:", len(df))
print("Столбцы:", df.columns.tolist())
print("Индексы:", df.index.tolist())
print("Типы данных:")
print(df.dtypes)

# === Первые и последние строки ===

print("\n=== Первые строки ===")
print(df.head())
print("\nПервые 2 строки:")
print(df.head(2))

print("\nПоследние строки:")
print(df.tail())

# === Создание DataFrame из списка списков ===

data_list = [
    [1, "Alice", 25],
    [2, "Bob", 30],
    [3, "Charlie", 35],
]

df_list = pd.DataFrame(
    data_list,
    columns=["id", "name", "age"]
)

print("\n=== DataFrame из списка списков ===")
print(df_list)

# === Создание DataFrame из NumPy массива ===

np_data = np.array([
    [25, 175, 70],
    [30, 165, 55],
    [35, 180, 85],
    [28, 170, 60],
])

df_numpy = pd.DataFrame(
    np_data,
    columns=["age", "height", "weight"]
)

print("\n=== DataFrame из NumPy массива ===")
print(df_numpy)