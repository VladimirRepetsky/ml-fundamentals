values = ["10", "20", "abc", "30", "xyz", "40"]

numbers = []
errors = []

for value in values:
    try:
        number = int(value)
        numbers.append(number)
    except ValueError:
        errors.append(value)

print("Исходные значения:", values)
print("Числа:", numbers)
print("Ошибочные значения:", errors)