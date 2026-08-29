text = input("Введите строку для обработки: ")

print("Исходная строка:")
print(text)

print("Первый символ:")
print(text[0])

print("Последний символ:")
print(text[-1])

print("Первые пять символов:")
print(text[:5])

print("Символы с 3 по 7:")
print(text[2:7])

print("Строка задом наперёд:")
print(text[::-1])

words = text.split()

if len(words) > 0:
    first_word = words[0]
    last_word = words[-1]

    print("Первое слово:")
    print(first_word)

    print("Последнее слово:")
    print(last_word)
else:
    print("Ты ввёл пустую строку")