"""
Сравнение трёх подходов к векторизации текста:
1. Bag of Words (частота)
2. TF (нормированная частота)
3. TF-IDF (частота × редкость)
"""
import numpy as np
import re

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^а-яёa-z0-9\s]', '', text)
    return re.sub(r'\s+', ' ', text).strip()

def text_to_words(text):
    return text.split()

def cosine_similarity(a, b):
    dot = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)

# Данные
documents = [
    "Кошка сидит на коврике",
    "Собака сидит на полу",
    "Кошка и собака друзья",
]
query = "кошка на коврике"

# Словарь
all_words = set()
for doc in documents:
    all_words.update(text_to_words(preprocess_text(doc)))
vocabulary = sorted(list(all_words))
word_to_index = {word: i for i, word in enumerate(vocabulary)}

# === 1. Bag of Words ===
def bow_vector(text):
    words = text_to_words(preprocess_text(text))
    vec = np.zeros(len(vocabulary))
    for word in words:
        if word in word_to_index:
            vec[word_to_index[word]] += 1
    return vec

# === 2. TF ===
def tf_vector(text):
    words = text_to_words(preprocess_text(text))
    vec = np.zeros(len(vocabulary))
    for word in words:
        if word in word_to_index:
            vec[word_to_index[word]] += 1
    if len(words) > 0:
        vec = vec / len(words)
    return vec

# === 3. TF-IDF ===
def tfidf_matrix(documents):
    n_docs = len(documents)
    matrix = np.zeros((n_docs, len(vocabulary)))
    idf = np.zeros(len(vocabulary))
    
    # IDF
    for i, word in enumerate(vocabulary):
        doc_count = sum(1 for doc in documents if word in text_to_words(preprocess_text(doc)))
        idf[i] = np.log((n_docs + 1) / (doc_count + 1)) + 1
    
    # TF-IDF
    for i, doc in enumerate(documents):
        words = text_to_words(preprocess_text(doc))
        for word in words:
            if word in word_to_index:
                matrix[i, word_to_index[word]] += 1
        if len(words) > 0:
            matrix[i] = matrix[i] / len(words)
        matrix[i] = matrix[i] * idf
    
    return matrix, idf

# Тестирование
print("=" * 60)
print("  СРАВНЕНИЕ: BoW vs TF vs TF-IDF")
print("=" * 60)

query_vec_bow = bow_vector(query)
query_vec_tf = tf_vector(query)
tfidf_mat, idf = tfidf_matrix(documents)
query_vec_tfidf = tf_vector(query) * idf

print(f"\nЗапрос: '{query}'")
print(f"Словарь: {vocabulary}")

print(f"\n--- Bag of Words ---")
for i, doc in enumerate(documents):
    sim = cosine_similarity(query_vec_bow, bow_vector(doc))
    print(f"  Документ {i+1}: {sim:.4f}")

print(f"\n--- TF ---")
for i, doc in enumerate(documents):
    sim = cosine_similarity(query_vec_tf, tf_vector(doc))
    print(f"  Документ {i+1}: {sim:.4f}")

print(f"\n--- TF-IDF ---")
for i, doc in enumerate(documents):
    sim = cosine_similarity(query_vec_tfidf, tfidf_mat[i])
    print(f"  Документ {i+1}: {sim:.4f}")

print(f"\n=== Вывод ===")
print("Для простого примера результаты похожи.")
print("Разница становится видна на больших корпусах,")
print("где есть частые слова ('и', 'на', 'в') и редкие термины.")
print("TF-IDF правильно понижает вес частых слов.")