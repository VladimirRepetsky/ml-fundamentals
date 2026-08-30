person = {
    "name": "Vladimir",
    "age": 25,
    "city": "Minsk",
    "is_learning_ml": True
}

print(person)
print(type(person))

# Доступ к значению по ключу
print(person["name"])
print(person["age"])
print(person["city"])

# Изменить значение
person["age"] = 26

# Добавить новую пару ключ-значение
person["profession"] = "ML Engineer"

print(person)

print(person.get("city"))
print(person.get("salary"))
print(person.get("salary", "Значение не найдено"))