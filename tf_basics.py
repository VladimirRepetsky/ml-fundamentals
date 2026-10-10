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

# Словарь
vocabulary = sorted(set(
    word for doc in documents for word in text_to_words(doc)
))
word_to_index = {word: i for i, word in enumerate(vocabulary)}

print("=== TF (Term Frequency) ===")
print(f"Словарь ({len(vocabulary)} слов): {vocabulary}")

def compute_tf(text, vocabulary):
    """
    Вычисляет TF (частоту термина) для текста.
    TF = количество вхождений слова / общее количество слов
    """
    words = text_to_words(text)
    tf_vector = np.zeros(len(vocabulary))
    total_words = len(words)
    if total_words == 0:
        return tf_vector
    for word in words:
        if word in word_to_index:
            tf_vector[word_to_index[word]] += 1
    # Нормализация: делим на общее количество слов
    tf_vector = tf_vector / total_words
    return tf_vector

# Вычисляем TF для каждого документа
print("\nTF-векторы документов:")
tf_matrix = np.zeros((len(documents), len(vocabulary)))
for i, doc in enumerate(documents):
    tf = compute_tf(doc, vocabulary)
    tf_matrix[i] = tf
    print(f"  Документ {i+1}: '{doc}'")
    print(f"    TF: {np.round(tf, 3)}")

print(f"\nМатрица TF:")
print(np.round(tf_matrix, 3))

# === Сравнение: BoW vs TF ===
print("\n=== Сравнение: BoW vs TF ===")
long_doc = "кошка кошка кошка кошка кошка сидит на коврике"
short_doc = "кошка на ковре"

long_tf = compute_tf(preprocess_text(long_doc), vocabulary)
short_tf = compute_tf(preprocess_text(short_doc), vocabulary)

print(f"Длинный документ: '{long_doc}'")
print(f"  TF: {np.round(long_tf, 3)}")
print(f"Короткий документ: '{short_doc}'")
print(f"  TF: {np.round(short_tf, 3)}")
print("\nTF нормализует по длине документа.")
print("Но всё ещё не учитывает редкость слова в коллекции!")