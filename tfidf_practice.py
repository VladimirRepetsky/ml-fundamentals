"""
Итоговые практические задания Дня 18.
Эти задания закрывают тему 'Векторизация текста' из Недели 3.
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

print("=" * 60)
print("  ИТОГОВЫЕ ЗАДАНИЯ ДНЯ 18")
print("=" * 60)

# ============================================================
# Задание 1: Построение словаря
# ============================================================
print("\n--- Задание 1: Построение словаря ---")
docs = [
    "машинное обучение это наука",
    "глубокое обучение использует нейросети",
    "наука о данных включает машинное обучение",
]
vocab = sorted(set(
    word for doc in docs for word in text_to_words(preprocess_text(doc))
))
print(f"Документы: {docs}")
print(f"Словарь ({len(vocab)} слов): {vocab}")

# ============================================================
# Задание 2: Векторизация через Bag of Words
# ============================================================
print("\n--- Задание 2: Bag of Words ---")
word_to_index = {w: i for i, w in enumerate(vocab)}

def bow_vector(text):
    words = text_to_words(preprocess_text(text))
    vec = np.zeros(len(vocab))
    for word in words:
        if word in word_to_index:
            vec[word_to_index[word]] += 1
    return vec

for doc in docs:
    vec = bow_vector(doc)
    print(f"  '{doc}' → {vec.astype(int)}")

# ============================================================
# Задание 3: Вычисление IDF
# ============================================================
print("\n--- Задание 3: IDF ---")
n_docs = len(docs)
idf = np.zeros(len(vocab))
for i, word in enumerate(vocab):
    doc_count = sum(1 for doc in docs if word in text_to_words(preprocess_text(doc)))
    idf[i] = np.log((n_docs + 1) / (doc_count + 1)) + 1

print(f"{'Слово':<15} {'Документов':<12} {'IDF'}")
print("-" * 42)
for word, idf_val in zip(vocab, idf):
    doc_count = sum(1 for doc in docs if word in text_to_words(preprocess_text(doc)))
    print(f"{word:<15} {doc_count:<12} {idf_val:.4f}")

# ============================================================
# Задание 4: Вычисление TF-IDF
# ============================================================
print("\n--- Задание 4: TF-IDF ---")
tfidf_matrix = np.zeros((n_docs, len(vocab)))
for i, doc in enumerate(docs):
    words = text_to_words(preprocess_text(doc))
    for word in words:
        if word in word_to_index:
            tfidf_matrix[i, word_to_index[word]] += 1
    if len(words) > 0:
        tfidf_matrix[i] /= len(words)
    tfidf_matrix[i] *= idf

print("Матрица TF-IDF:")
print(np.round(tfidf_matrix, 4))

# ============================================================
# Задание 5: Поиск похожего документа
# ============================================================
print("\n--- Задание 5: Поиск похожего документа ---")
query = "машинное обучение и нейросети"
query_vec = bow_vector(query)
query_vec = query_vec / max(len(text_to_words(preprocess_text(query))), 1) * idf

print(f"Запрос: '{query}'")
print(f"Вектор запроса: {np.round(query_vec, 4)}")
print(f"\nКосинусное сходство:")
for i, doc in enumerate(docs):
    sim = cosine_similarity(query_vec, tfidf_matrix[i])
    print(f"  Документ {i+1}: {sim:.4f} — '{doc}'")

best_idx = np.argmax([
    cosine_similarity(query_vec, tfidf_matrix[i]) for i in range(n_docs)
])
print(f"\n✅ Наиболее похожий: Документ {best_idx + 1}")

# ============================================================
# Итоги
# ============================================================
print("\n" + "=" * 60)
print("  ИТОГИ ДНЯ 18")
print("=" * 60)
print("""
✅ Понимаю проблему представления текста в виде чисел
✅ Реализовал Bag of Words с нуля
✅ Понимаю ограничения Bag of Words
✅ Вычисляю TF (частоту термина)
✅ Вычисляю IDF (обратную частоту документа)
✅ Вычисляю TF-IDF = TF × IDF
✅ Реализовал TF-IDF с нуля на NumPy
✅ Написал мини-поисковик на TF-IDF + косинус
✅ Понимаю, когда использовать TF-IDF

Это закрывает тему 'Векторизация текста' из Недели 3.
""")