def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль"

    return a / b


while True:
    print("\n--- Калькулятор ---")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Выйти")

    choice = input("Выберите действие: ")

    if choice == "5":
        print("До свидания!")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Неверный выбор.")
        continue

    first = input("Введите первое число: ")
    second = input("Введите второе число: ")

    if not first.replace(".", "", 1).isdigit() or not second.replace(".", "", 1).isdigit():
        print("Пожалуйста, введите корректное число.")
        continue

    a = float(first)
    b = float(second)

    if choice == "1":
        result = add(a, b)
        operation = "+"
    elif choice == "2":
        result = subtract(a, b)
        operation = "-"
    elif choice == "3":
        result = multiply(a, b)
        operation = "*"
    else:
        result = divide(a, b)
        operation = "/"

    print(f"{a} {operation} {b} = {result}")