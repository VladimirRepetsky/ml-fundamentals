import numpy as np
import re

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^а-яёa-z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def text_to_words(text):
    return text.split()

# Данные
documents_raw = [
    "Кошка сидит на коврике.",
    "Собака сидит на полу!",
    "Кошка и собака — друзья.",
]
documents = [preprocess_text(doc) for doc in documents_raw]

vocabulary = sorted(set(
    word for doc in documents for word in text_to_words(doc)
))
word_to_index = {word: i for i, word in enumerate(vocabulary)}

print("=== IDF (Inverse Document Frequency) ===")
print(f"Количество документов: {len(documents)}")
print(f"Словарь ({len(vocabulary)} слов): {vocabulary}")

def compute_idf(documents, vocabulary):
    """
    Вычисляет IDF для каждого слова в словаре.
    IDF = log(N / df), где:
        N = общее количество документов
        df = количество документов, содержащих слово
    """
    n_docs = len(documents)
    idf_vector = np.zeros(len(vocabulary))
    for i, word in enumerate(vocabulary):
        # Считаем, в скольких документах встречается слово
        doc_count = 0
        for doc in documents:
            words = text_to_words(doc)
            if word in words:
                doc_count += 1
        # IDF = log(N / df)
        # Добавляем 1 для сглаживания: log((N + 1) / (df + 1)) + 1
        idf_vector[i] = np.log((n_docs + 1) / (doc_count + 1)) + 1
    return idf_vector

idf = compute_idf(documents, vocabulary)

print("\nIDF для каждого слова:")
print(f"{'Слово':<12} {'Документов':<12} {'IDF'}")
print("-" * 40)
for i, word in enumerate(vocabulary):
    doc_count = sum(1 for doc in documents if word in text_to_words(doc))
    print(f"{word:<12} {doc_count:<12} {idf[i]:.4f}")

print("\n=== Интерпретация ===")
print("Слова, которые встречаются во ВСЕХ документах → низкий IDF")
print("Слова, которые встречаются РЕДКО → высокий IDF")
print("\nПример:")
print("  'сидит' — в 2 из 3 документов → средний IDF")
print("  'и' — в 1 из 3 документов → более высокий IDF")
print("  'коврике' — в 1 из 3 документов → более высокий IDF")
print("  'на' — в 2 из 3 документов → средний IDF")

# === Визуальное сравнение ===
print("\n=== Сравнение весов слов ===")
for word in ["сидит", "и", "коврике", "кошка"]:
    if word in word_to_index:
        idx = word_to_index[word]
        doc_count = sum(1 for doc in documents if word in text_to_words(doc))
        print(f"  '{word}': встречается в {doc_count}/{len(documents)} документах, IDF = {idf[idx]:.4f}")