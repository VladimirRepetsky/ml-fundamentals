def count_words(words):
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


text = input("Введите текст: ")

words = text.lower().split()

result = count_words(words)

print("\nЧастота слов:")
for word, count in result.items():
    print(f"{word}: {count}")