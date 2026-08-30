fruits = {"apple", "banana"}

# Добавить элемент
fruits.add("cherry")
print(fruits)

# Добавить несколько элементов
fruits.update(["mango", "orange"])
print(fruits)

# Удалить элемент
fruits.remove("banana")
print(fruits)

# Безопасное удаление: не вызывает ошибку, если элемента нет
fruits.discard("banana")
print(fruits)

# Проверка наличия
print("apple" in fruits)
print("banana" in fruits)