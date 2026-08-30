person = {
    "name": "Vladimir",
    "age": 25,
    "city": "Moscow",
    "language": "Python"
}

print(person)

# Удалить по ключу и вернуть значение
removed_value = person.pop("city")
print("Удалено:", removed_value)
print(person)

# Удалить последнюю добавленную пару
last_item = person.popitem()
print("Последняя удалённая пара:", last_item)
print(person)

# Очистить словарь
person.clear()
print(person)

