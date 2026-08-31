from functools import reduce

PUNCTUATION = ".,!?;:()\"'«»—"

STOP_WORDS = {
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
    "он",
    "она",
    "оно",
    "они",
    "был",
    "была",
    "было",
    "бы",
    "мы",
    "вы",
    "ты",
    "я",
    "за",
    "то",
    "же",
    "ли",
    "быть",
    "этот",
    "эта",
    "эти"
}


def clean_text(text):
    """
    Очищает текст: переводит в нижний регистр и убирает пунктуацию.
    """
    text = text.lower()

    for char in PUNCTUATION:
        text = text.replace(char, "")

    return text


def get_words(text):
    """
    Разбивает текст на список слов.
    """
    words = text.split()

    return list(map(lambda word: word.strip(), words))


def remove_stop_words(words, *stop_words):
    """
    Удаляет стоп-слова из списка слов.
    """
    stop_set = set(stop_words)

    filtered_words = list(
        filter(lambda word: word not in stop_set, words)
    )

    return filtered_words


def count_words(words):
    """
    Считает частоту каждого слова.
    """
    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency


def get_top_words(frequency, top_n=5):
    """
    Возвращает топ слов по частоте.
    """
    sorted_words = sorted(
        frequency.items(),
        key=lambda item: item[1],
        reverse=True
    )

    return sorted_words[:top_n]


def calculate_total_chars(words):
    """
    Считает суммарную длину всех слов.
    """
    total = reduce(lambda acc, word: acc + len(word), words, 0)

    return total


def build_report(text, **options):
    """
    Собирает полный отчёт по тексту.
    """
    top_n = options.get("top_n", 5)
    stop_words = options.get("stop_words", STOP_WORDS)

    cleaned_text = clean_text(text)
    all_words = get_words(cleaned_text)
    filtered_words = remove_stop_words(all_words, *stop_words)

    frequency_all = count_words(all_words)
    frequency_filtered = count_words(filtered_words)

    top_words = get_top_words(frequency_filtered, top_n)

    report = {
        "cleaned_text": cleaned_text,
        "total_words": len(all_words),
        "unique_words": len(set(all_words)),
        "filtered_words_count": len(filtered_words),
        "unique_filtered_words": len(set(filtered_words)),
        "total_chars_in_filtered_words": calculate_total_chars(filtered_words),
        "top_words": top_words
    }

    return report


def print_report(report, **metadata):
    """
    Красиво печатает отчёт.
    """
    print("=" * 60)

    if metadata:
        for key, value in metadata.items():
            print(f"{key}: {value}")

        print("=" * 60)

    for key, value in report.items():
        if key == "top_words":
            print("top_words:")

            for word, count in value:
                print(f"    {word}: {count}")
        else:
            print(f"{key}: {value}")

    print("=" * 60)


text = """
Машинное обучение изучает данные и алгоритмы.
Данные важны для машинного обучения, потому что данные помогают моделям учиться.
Машинное обучение и анализ данных используют алгоритмы, данные и модели.
"""

report = build_report(text, top_n=5, stop_words=STOP_WORDS)

print_report(
    report,
    title="Text Analytics Report",
    author="Vladimir",
    day=9,
    block="Functions"
)