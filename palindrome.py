word = input("Введите слово для проверки на палиндром: ")

clean_word = word.strip().lower()
reversed_word = clean_word[::-1]

print(f"Слово: {clean_word}")
print(f"Слово наоборот: {reversed_word}")

if clean_word == reversed_word:
    print("Это палиндром")
else:
    print("Это не палиндром")