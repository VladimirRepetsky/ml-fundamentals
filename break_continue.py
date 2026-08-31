numbers = [1, 3, 4, 7, 8, 10, 15, 21]

print("Нечётные числа:")

for number in numbers:
    if number % 2 == 0:
        continue

    print(number)

    numbers = [1, 3, 4, 7, 8, 10, 15, 21]

target = 7
found = False

for number in numbers:
    if number == target:
        found = True
        break

if found:
    print(f"\nЧисло {target} найдено")
else:
    print(f"\nЧисло {target} не найдено")