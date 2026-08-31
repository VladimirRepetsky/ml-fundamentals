text = input("Введите текст для анализа: ")

text = text.lower()

for char in ".,!?;:()\"'":
    text = text.replace(char, "")

words = text.split()

stop_words = {
    "и",
    "в",
    "на",
    "с",
    "по",
    "не",
    "а",
    "но",
    "из",
    "к",
    "у",
    "о",
    "про",
    "это",
    "как",
    "что",
    "был",
    "была",
    "было"
}

filtered_words = []

for word in words:
    if word not in stop_words:
        filtered_words.append(word)

frequency = {}

for word in filtered_words:
    frequency[word] = frequency.get(word, 0) + 1

print("\nВсе слова после удаления стоп-слов:")
print(filtered_words)

print("\nЧастота слов:")

for word, count in frequency.items():
    print(f"{word}: {count}")

print("\nКоличество уникальных слов:", len(frequency))

top_words = sorted(
    frequency.items(),
    key=lambda item: item[1],
    reverse=True
)

print("\nТоп-5 слов:")

for word, count in top_words[:5]:
    print(f"{word}: {count}")