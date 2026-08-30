# Создание множества
fruits = {"apple", "banana", "cherry"}

print(fruits)
print(type(fruits))

# Множество автоматически убирает дубликаты
numbers = {1, 2, 2, 3, 3, 3, 4, 4, 4, 4}

print(numbers)

numbers_list = [1, 2, 2, 3, 4, 4, 5]

unique_numbers = set(numbers_list)

print("Список:", numbers_list)
print("Множество:", unique_numbers)
print("Обратно список:", list(unique_numbers))