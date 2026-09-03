import numpy as np

# === Представление данных в виде матрицы признаков ===

# Допустим, у нас есть данные о 5 студентах:
# - возраст
# - количество часов обучения в день
# - балл за экзамен

students = np.array([
    [22, 3, 75],
    [25, 5, 88],
    [23, 2, 65],
    [30, 6, 92],
    [28, 4, 80],
])

feature_names = ["возраст", "часы_обучения", "балл"]

print("=== Матрица признаков ===")
print("Данные о студентах:")
print(students)
print("Форма:", students.shape)
print("Признаки:", feature_names)

# === Задание 1: Транспонируйте матрицу ===

print("\n=== Задание 1: Транспонирование ===")
transposed = students.T
print("Транспонированная матрица:")
print(transposed)
print("Форма:", transposed.shape)
print("Теперь каждая строка — это признак:")
for i, name in enumerate(feature_names):
    print(f"  {name}: {transposed[i]}")

# === Задание 2: Среднее значение для каждого столбца ===

print("\n=== Задание 2: Среднее по каждому признаку ===")
mean_per_feature = np.mean(students, axis=0)
print("Среднее по каждому признаку:")
for name, value in zip(feature_names, mean_per_feature):
    print(f"  {name}: {value:.2f}")

# === Задание 3: Матричное умножение на транспонированную ===

print("\n=== Задание 3: X @ X.T ===")

# Возьмём подматрицу без балла (только признаки)
X = students[:, :2]  # возраст и часы обучения
print("Матрица признаков (возраст, часы):")
print(X)
print("Форма:", X.shape)

# X @ X.T
XXt = X @ X.T
print("\nX @ X.T:")
print(XXt)
print("Форма:", XXt.shape)

# X.T @ X
XtX = X.T @ X
print("\nX.T @ X:")
print(XtX)
print("Форма:", XtX.shape)

# === Задание 4: Евклидово расстояние между строками ===

print("\n=== Задание 4: Евклидово расстояние ===")

def euclidean_distance(a, b):
    """
    Вычисляет евклидово расстояние между двумя векторами.
    Это основа алгоритма KNN.
    """
    return np.sqrt(np.sum((a - b) ** 2))

# Расстояние между первым и вторым студентом (по признакам возраст и часы)
student_1 = X[0]
student_2 = X[1]

distance = euclidean_distance(student_1, student_2)
print(f"Студент 1: {student_1}")
print(f"Студент 2: {student_2}")
print(f"Евклидово расстояние: {distance:.2f}")

# Расстояния от первого студента до всех остальных
print("\nРасстояния от студента 1 до всех остальных:")
for i in range(len(X)):
    dist = euclidean_distance(X[0], X[i])
    print(f"  До студента {i+1}: {dist:.2f}")

# === Нормализация матрицы признаков ===

print("\n=== Нормализация признаков ===")
print("Зачем: признаки имеют разный масштаб.")
print("Возраст ~22-30, часы ~2-6, балл ~65-92.")
print("Модель может придавать больший вес признаку с большим диапазоном.")

# Нормализация: (x - min) / (max - min)
X_min = np.min(X, axis=0)
X_max = np.max(X, axis=0)
X_normalized = (X - X_min) / (X_max - X_min)

print("\nИсходная матрица:")
print(X)
print("\nНормализованная матрица:")
print(np.round(X_normalized, 3))

# Проверка: минимум 0, максимум 1
print("\nПроверка:")
print("Минимум по столбцам:", np.min(X_normalized, axis=0))
print("Максимум по столбцам:", np.max(X_normalized, axis=0))

# === Стандартизация матрицы признаков ===

print("\n=== Стандартизация признаков ===")

X_mean = np.mean(X, axis=0)
X_std = np.std(X, axis=0)
X_standardized = (X - X_mean) / X_std

print("Стандартизированная матрица:")
print(np.round(X_standardized, 3))

print("\nПроверка:")
print("Среднее по столбцам:", np.round(np.mean(X_standardized, axis=0), 10))
print("Стд по столбцам:", np.round(np.std(X_standardized, axis=0), 10))