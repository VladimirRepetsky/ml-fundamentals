fruits = ["apple", "banana"]

# Добавить один элемент в конец
fruits.append("cherry")
print(fruits)

# Вставить элемент по индексу
fruits.insert(1, "blueberry")
print(fruits)

# Удалить элемент по значению
fruits.remove("banana")
print(fruits)

# Удалить элемент по индексу и вернуть его
removed_item = fruits.pop(0)
print("Удалено:", removed_item)
print(fruits)

# Очистить список полностью
fruits.clear()
print(fruits)

numbers = [3, 1, 4, 1, 5, 9, 2, 6]

print("Минимум:", min(numbers))
print("Максимум:", max(numbers))
print("Сумма:", sum(numbers))
print("Длина:", len(numbers))
print("Среднее:", sum(numbers) / len(numbers))

# Сортировка
sorted_numbers = sorted(numbers)
print("Отсортированный:", sorted_numbers)
print("Исходный не изменился:", numbers)

# Сортировка на месте
numbers.sort()
print("После sort():", numbers)

# Разворот
numbers.reverse()
print("После reverse():", numbers)