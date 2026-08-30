text = input("Введите текст: ")

words = text.lower().split()

unique_words = set(words)

print("Все слова:", words)
print("Уникальные слова:", unique_words)
print("Количество уникальных слов:", len(unique_words))

unique_words_sorted = sorted(unique_words)

print("Уникальные слова по алфавиту:")
for word in unique_words_sorted:
    print(word)