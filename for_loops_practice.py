numbers = [3, 5, 8, 12, 7]

total = 0

for number in numbers:
    total += number

print("Список:", numbers)
print("Сумма элементов:", total)

print("Числа от 1 до 10:")

for i in range(1, 11):
    print(i)

print("Числа от 0 до 100 с шагом 10:")

for i in range(0, 101, 10):
    print(i)

print("Обратный отсчёт:")

for i in range(10, 0, -1):
    print(i)

print("Старт!")