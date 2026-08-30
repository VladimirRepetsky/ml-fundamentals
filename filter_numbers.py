numbers = [12, -7, 5, 64, -1, 0, 33, 8, -15, 100]

positive = []
negative = []
zeros = []
even = []
odd = []

for number in numbers:
    if number > 0:
        positive.append(number)
    elif number < 0:
        negative.append(number)
    else:
        zeros.append(number)

    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

print("Исходные числа:")
print(numbers)

print("\nПоложительные:")
print(positive)

print("Отрицательные:")
print(negative)

print("Нули:")
print(zeros)

print("Чётные:")
print(even)

print("Нечётные:")
print(odd)