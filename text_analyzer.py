text = input("Введите любой текст: ")

length = len(text)
words = text.split()
word_count = len(words)

print("Ты ввёл текст:")
print(text)

print(f"Длина текста: {length} символов")
print(f"Количество слов: {word_count}")

print("Текст в верхнем регистре:")
print(text.upper())

print("Текст в нижнем регистре:")
print(text.lower())