lines = [
    "Первая строка",
    "Вторая строка",
    "Третья строка"
]

with open("data.txt", "w", encoding="utf-8") as file:
    for line in lines:
        file.write(line + "\n")

print("Файл data.txt успешно записан.")

with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()

print("Содержимое файла:")
print(content)

print("Чтение построчно:")

with open("data.txt", "r", encoding="utf-8") as file:
    for index, line in enumerate(file, start=1):
        print(f"{index}. {line.strip()}")

with open("data.txt", "a", encoding="utf-8") as file:
    file.write("Четвёртая строка\n")
    file.write("Пятая строка\n")

print("Данные дозаписаны в файл.")

try:
    with open("missing.txt", "r", encoding="utf-8") as file:
        content = file.read()
except FileNotFoundError:
    print("Ошибка: файл missing.txt не найден.")

