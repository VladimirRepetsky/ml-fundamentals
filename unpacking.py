def add_three(a, b, c):
    return a + b + c


numbers = [1, 2, 3]

print(add_three(numbers[0], numbers[1], numbers[2]))
print(add_three(*numbers))

def show_user(name, age, city):
    print("Имя:", name)
    print("Возраст:", age)
    print("Город:", city)
    print("-" * 30)


user = {
    "name": "Vladimir",
    "age": 25,
    "city": "Moscow"
}

show_user(**user)

