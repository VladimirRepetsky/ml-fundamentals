try:
    number = int(input("Введите число: "))
    print("Вы ввели:", number)
except ValueError:
    print("Ошибка: это не число.")


try:
    number = int(input("Введите число: "))
    result = 100 / number
    print("Результат:", result)
except ValueError:
    print("Ошибка: нужно ввести число.")
except ZeroDivisionError:
    print("Ошибка: нельзя делить на ноль.")

try:
    number = int(input("Введите число для деления 100: "))
    result = 100 / number
except ValueError:
    print("Ошибка: это не число.")
except ZeroDivisionError:
    print("Ошибка: нельзя делить на ноль.")
else:
    print("Ошибок не было.")
    print("Результат:", result)
finally:
    print("Блок завершён.")


