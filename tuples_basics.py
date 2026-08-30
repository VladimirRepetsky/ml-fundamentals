# Создание кортежей
coordinates = (10, 20)
colors = ("red", "green", "blue")
single_element = (42,)   # запятая обязательна для кортежа из одного элемента
empty_tuple = ()

print(coordinates)
print(colors)
print(single_element)
print(type(single_element))

# Доступ по индексу работает так же, как у списков
print(coordinates[0])
print(colors[-1])

# Длина кортежа
print(len(colors))

my_list = [1, 2, 3]
my_tuple = (1, 2, 3)

# И список, и кортеж можно перебирать
for item in my_list:
    print("list:", item)

for item in my_tuple:
    print("tuple:", item)

# Список можно менять
my_list[0] = 99
print("Изменённый список:", my_list)

# Кортеж менять нельзя — будет ошибка
# my_tuple[0] = 99