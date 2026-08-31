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

    try:
        a = float(first)
        b = float(second)

        if choice == "1":
            result = a + b
            operation = "+"
        elif choice == "2":
            result = a - b
            operation = "-"
        elif choice == "3":
            result = a * b
            operation = "*"
        else:
            result = a / b
            operation = "/"

    except ValueError:
        print("Ошибка: нужно ввести число.")
    except ZeroDivisionError:
        print("Ошибка: делить на ноль нельзя.")
    else:
        print(f"{a} {operation} {b} = {result}")
    finally:
        print("Операция завершена.")