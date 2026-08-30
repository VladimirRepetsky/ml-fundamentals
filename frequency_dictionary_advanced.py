def count_words(words):
    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency


def print_frequency(frequency):
    for word, count in frequency.items():
        print(f"{word}: {count}")


def print_top_words(frequency, top_n=5):
    sorted_words = sorted(frequency.items(), key=lambda item: item[1], reverse=True)

    print(f"\nТоп-{top_n} слов:")
    for word, count in sorted_words[:top_n]:
        print(f"{word}: {count}")


text = input("Введите текст: ")

words = text.lower().split()

frequency = count_words(words)

print("\nВсе слова:")
print_frequency(frequency)

print_top_words(frequency, top_n=3)