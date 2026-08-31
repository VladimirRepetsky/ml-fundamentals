def add(a, b):
    result = a + b
    return result


sum_value = add(3, 5)

print("Результат сложения:", sum_value)

def add_with_print(a, b):
    print(a + b)


def add_with_return(a, b):
    return a + b


result1 = add_with_print(10, 20)
result2 = add_with_return(10, 20)

print("result1:", result1)
print("result2:", result2)

def say_hello():
    print("Hello")


result = say_hello()

print("Значение результата:", result)

def check_age(age):
    if age < 0:
        return "Возраст не может быть отрицательным"

    if age >= 18:
        return "Совершеннолетний"
    else:
        return "Несовершеннолетний"


print(check_age(25))
print(check_age(15))
print(check_age(-5))

def get_statistics(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    total = sum(numbers)

    return minimum, maximum, total


data = [10, 20, 30, 40, 50]

min_value, max_value, total_value = get_statistics(data)

print("Минимум:", min_value)
print("Максимум:", max_value)
print("Сумма:", total_value)

