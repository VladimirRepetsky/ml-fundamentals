text = input("Введите любой текст: ")

search_symbol = input("Введите символ или букву для подсчёта: ")

length = len(text)
words = text.split()
word_count = len(words)
symbol_count = text.count(search_symbol)

print(f"Длина текста: {length} символов")
print(f"Количество слов: {word_count}")
print(f"Символ '{search_symbol}' встречается {symbol_count} раз(а)")

print("Первые 10 символов текста:")
print(text[:10])

print("Последние 10 символов текста:")
print(text[-10:])