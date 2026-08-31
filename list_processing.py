numbers = [12, -7, 5, 64, -1, 0, 33, 8, -15, 100]

positive_count = 0
negative_count = 0
zero_count = 0

even_count = 0
odd_count = 0

positive_sum = 0
negative_sum = 0

for number in numbers:
    if number > 0:
        positive_count += 1
        positive_sum += number
    elif number < 0:
        negative_count += 1
        negative_sum += number
    else:
        zero_count += 1

    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Исходный список:")
print(numbers)

print("\nПоложительных:", positive_count)
print("Отрицательных:", negative_count)
print("Нулей:", zero_count)

print("Чётных:", even_count)
print("Нечётных:", odd_count)

print("Сумма положительных:", positive_sum)
print("Сумма отрицательных:", negative_sum)

numbers = [12, -7, 5, 64, -1, 0, 33, 8, -15, 100]

max_value = numbers[0]
min_value = numbers[0]

for number in numbers:
    if number > max_value:
        max_value = number

    if number < min_value:
        min_value = number

print("\nМаксимум:", max_value)
print("Минимум:", min_value)

prices = [100, 250, 50, 800]

discounted_prices = []

for price in prices:
    discounted_prices.append(price * 0.9)

print("\nИсходные цены:")
print(prices)

print("Цены со скидкой 10%:")
print(discounted_prices)