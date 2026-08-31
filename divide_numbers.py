def get_number(prompt):
    while True:
        value = input(prompt)

        try:
            return float(value)
        except ValueError:
            print("Пожалуйста, введите корректное число.")


while True:
    print("\n--- Деление двух чисел ---")

    a = get_number("Введите первое число: ")
    b = get_number("Введите второе число: ")

    try:
        result = a / b
    except ZeroDivisionError:
        print("Ошибка: делить на ноль нельзя.")
    else:
        print(f"{a} / {b} = {result}")
    finally:
        print("Операция завершена.")

    again = input("Выполнить ещё раз? (да/нет): ").strip().lower()

    if again != "да":
        print("До свидания!")
        break

