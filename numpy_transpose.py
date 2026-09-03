import numpy as np

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
])

print("Исходная матрица:")
print(matrix)
print("Форма:", matrix.shape)

# === Транспонирование ===
# Строки становятся столбцами, столбцы становятся строками

transposed = matrix.T
print("\nТранспонированная матрица:")
print(transposed)
print("Форма:", transposed.shape)

# Альтернативный способ
transposed2 = np.transpose(matrix)
print("\nnp.transpose(matrix):")
print(transposed2)
print("Форма:", transposed2.shape)

# === Свойство транспонирования ===

print("\n=== Свойства ===")
print("Двойное транспонирование возвращает оригинал:")
print(matrix.T.T)
print("Равно оригиналу:", np.array_equal(matrix.T.T, matrix))

# === Практический пример ===

print("\n=== Практический пример ===")

# Данные: 3 человека × 2 признака
people = np.array([
    [25, 175],
    [30, 165],
    [35, 180],
])

print("Исходные данные (люди × признаки):")
print(people)
print("Форма:", people.shape)

transposed_people = people.T
print("\nТранспонированные данные (признаки × люди):")
print(transposed_people)
print("Форма:", transposed_people.shape)

print("\nТеперь каждая строка — это признак:")
print("  Возраст:", transposed_people[0])
print("  Рост:", transposed_people[1])

# === Транспонирование и матричное умножение ===
# Это будет важно в следующем шаге

print("\n=== Подготовка к матричному умножению ===")
A = np.array([[1, 2], [3, 4], [5, 6]])
print("A:")
print(A)
print("A.shape:", A.shape)

print("\nA.T:")
print(A.T)
print("A.T.shape:", A.T.shape)

# Умножение A на A.T
result = A @ A.T
print("\nA @ A.T:")
print(result)
print("Форма:", result.shape)

# Умножение A.T на A
result2 = A.T @ A
print("\nA.T @ A:")
print(result2)
print("Форма:", result2.shape)