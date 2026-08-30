numbers = []

count = int(input("Сколько чисел вы хотите ввести? "))

for i in range(count):
    value = float(input(f"Введите число {i + 1}: "))
    numbers.append(value)

print("\nВы ввели числа:", numbers)
print("Минимум:", min(numbers))
print("Максимум:", max(numbers))
print("Сумма:", sum(numbers))
print("Среднее:", sum(numbers) / len(numbers))

# Отсортированный список
print("По возрастанию:", sorted(numbers))
print("По убыванию:", sorted(numbers, reverse=True))