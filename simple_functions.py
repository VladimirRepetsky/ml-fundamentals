def square(number):
    return number ** 2


def is_even(number):
    return number % 2 == 0


def is_positive(number):
    return number > 0


def max_of_two(a, b):
    if a > b:
        return a
    return b


def max_of_three(a, b, c):
    maximum = a

    if b > maximum:
        maximum = b

    if c > maximum:
        maximum = c

    return maximum


print(square(5))
print(is_even(10))
print(is_even(7))
print(is_positive(-3))
print(max_of_two(15, 8))
print(max_of_three(10, 25, 17))

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(25))
print(fahrenheit_to_celsius(77))

def calculate_discount(price, discount_percent):
    discount = price * discount_percent / 100
    final_price = price - discount
    return final_price


print(calculate_discount(1000, 10))
print(calculate_discount(500, 20))

def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


print(get_grade(95))
print(get_grade(82))
print(get_grade(67))
print(get_grade(50))