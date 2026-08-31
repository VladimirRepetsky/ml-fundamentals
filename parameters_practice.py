def create_profile(name, age, city):
    print(f"Имя: {name}")
    print(f"Возраст: {age}")
    print(f"Город: {city}")
    print("-" * 30)


# Позиционные аргументы
create_profile("Vladimir", 25, "Moscow")

# Именованные аргументы
create_profile(name="Alice", age=30, city="Berlin")

# Смешанный вызов
create_profile("Bob", city="Paris", age=22)

def create_user(name, age, profession="Developer", country="Unknown"):
    print(f"Имя: {name}")
    print(f"Возраст: {age}")
    print(f"Профессия: {profession}")
    print(f"Страна: {country}")
    print("-" * 30)


create_user("Vladimir", 25)
create_user("Alice", 30, "Data Scientist")
create_user("Bob", 22, "ML Engineer", "Germany")

def add_item_bad(item, items=[]):
    items.append(item)
    return items


print(add_item_bad("apple"))
print(add_item_bad("banana"))
print(add_item_bad("orange"))

