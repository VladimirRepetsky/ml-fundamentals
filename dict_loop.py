person = {
    "name": "Vladimir",
    "age": 25,
    "city": "Moscow"
}

# Перебор ключей
for key in person:
    print(key)

# Перебор значений
for value in person.values():
    print(value)

# Перебор пар ключ-значение
for key, value in person.items():
    print(key, "->", value)