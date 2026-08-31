numbers = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x ** 2, numbers))

print("Исходные числа:", numbers)
print("Квадраты:", squared)

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


temperatures_c = [0, 10, 20, 25, 30]

temperatures_f = list(map(celsius_to_fahrenheit, temperatures_c))

print("\nЦельсий:", temperatures_c)
print("Фаренгейт:", temperatures_f)

numbers = [12, -7, 5, 64, -1, 0, 33, 8]

positive = list(filter(lambda x: x > 0, numbers))
negative = list(filter(lambda x: x < 0, numbers))
even = list(filter(lambda x: x % 2 == 0, numbers))

print("\nИсходные числа:", numbers)
print("Положительные:", positive)
print("Отрицательные:", negative)
print("Чётные:", even)

from functools import reduce

numbers = [1, 2, 3, 4, 5]

total = reduce(lambda acc, x: acc + x, numbers, 0)

print("\nИсходные числа:", numbers)
print("Сумма через reduce:", total)

numbers = [1, 2, 3, 4, 5]

product = reduce(lambda acc, x: acc * x, numbers, 1)

print("Произведение через reduce:", product)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared = list(map(lambda x: x ** 2, numbers))
even = list(filter(lambda x: x % 2 == 0, numbers))
total = reduce(lambda acc, x: acc + x, numbers, 0)

print("\nИсходные числа:", numbers)
print("Квадраты:", squared)
print("Чётные:", even)
print("Сумма:", total)