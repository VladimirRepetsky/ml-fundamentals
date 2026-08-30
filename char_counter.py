def count_chars(text):
    chars = {}

    for char in text:
        if char == " ":
            continue

        chars[char] = chars.get(char, 0) + 1

    return chars


text = input("Введите текст: ")

result = count_chars(text.lower())

print("\nЧастота символов:")
for char, count in result.items():
    print(f"'{char}': {count}")