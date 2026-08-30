# Создание списков
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True]
empty = []

print(numbers)
print(fruits)
print(mixed)
print(empty)

# Тип переменной
print(type(numbers))

fruits = ["apple", "banana", "cherry", "date"]

print(fruits[0])    # первый элемент
print(fruits[1])    # второй элемент
print(fruits[-1])   # последний элемент
print(fruits[-2])   # предпоследний элемент

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[0:5])    # первые пять элементов
print(numbers[5:])     # с пятого индекса до конца
print(numbers[:5])     # сначала до пятого индекса
print(numbers[::2])    # каждый второй элемент
print(numbers[::-1])   # список наоборот

