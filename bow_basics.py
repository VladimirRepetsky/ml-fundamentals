import numpy as np
import re

# ============================================================
# ПРЕДОБРАБОТКА ТЕКСТА
# ============================================================

def preprocess_text(text):
    """
    Предобработка текста для векторизации.
    1. Приведение к нижнему регистру.
    2. Удаление пунктуации.
    3. Удаление лишних пробелов.
    """
    # Нижний регистр
    text = text.lower()
    # Удаление пунктуации (оставляем только буквы и пробелы)
    text = re.sub(r'[^а-яёa-z0-9\s]', '', text)
    # Удаление лишних пробелов
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def text_to_words(text):
    """Разбивает текст на список слов."""
    return text.split()

# Тест
documents_raw = [
    "Кошка сидит на коврике.",
    "Собака сидит на полу!",
    "Кошка и собака — друзья.",
]

print("=== Предобработка текста ===")
documents = []
for doc in documents_raw:
    clean = preprocess_text(doc)
    words = text_to_words(clean)
    documents.append(clean)
    print(f"  Оригинал:  {doc}")
    print(f"  Очищенный: {clean}")
    print(f"  Слова:     {words}")
    print()

# === Построение словаря ===
print("=== Построение словаря ===")
vocabulary = set()
for doc in documents:
    words = text_to_words(doc)
    vocabulary.update(words)

vocabulary = sorted(list(vocabulary))
print(f"Размер словаря: {len(vocabulary)} слов")
print(f"Словарь: {vocabulary}")

# === Индекс слова ===
word_to_index = {word: i for i, word in enumerate(vocabulary)}
print(f"\nИндексы слов:")
for word, idx in word_to_index.items():
    print(f"  '{word}' → {idx}")


# ============================================================
# BAG OF WORDS
# ============================================================

def text_to_bow_vector(text, vocabulary):
    """
    Преобразует текст в вектор Bag of Words.
    Каждая координата — частота соответствующего слова из словаря.
    """
    words = text_to_words(text)
    vector = np.zeros(len(vocabulary))
    for word in words:
        if word in word_to_index:
            vector[word_to_index[word]] += 1
    return vector

print("\n=== Bag of Words ===")
print("Векторное представление документов:")
bow_vectors = []
for doc in documents:
    vec = text_to_bow_vector(doc, vocabulary)
    bow_vectors.append(vec)
    print(f"  '{doc}'")
    print(f"    → {vec.astype(int)}")

bow_matrix = np.array(bow_vectors)
print(f"\nМатрица BoW (документы × слова):")
print(bow_matrix.astype(int))
print(f"Форма: {bow_matrix.shape}")
print(f"  Строки = документы ({bow_matrix.shape[0]})")
print(f"  Столбцы = слова из словаря ({bow_matrix.shape[1]})")

# === Поиск похожего документа через косинус ===
def cosine_similarity(a, b):
    dot = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)

print("\n=== Поиск похожего документа ===")
query = "кошка на коврике"
query_clean = preprocess_text(query)
query_vector = text_to_bow_vector(query_clean, vocabulary)
print(f"Запрос: '{query}'")
print(f"Вектор запроса: {query_vector.astype(int)}")
print(f"\nКосинусное сходство с документами:")
for i, doc in enumerate(documents):
    sim = cosine_similarity(query_vector, bow_vectors[i])
    print(f"  Документ {i+1}: {sim:.4f} — '{doc}'")

best_idx = np.argmax([cosine_similarity(query_vector, v) for v in bow_vectors])
print(f"\nНаиболее похожий документ: Документ {best_idx + 1}")


# ============================================================
# ОГРАНИЧЕНИЯ BAG OF WORDS
# ============================================================

print("\n=== Ограничения Bag of Words ===")

# Проблема 1: частые слова доминируют
print("\nПроблема 1: Частые слова доминируют")
long_doc = "кошка кошка кошка кошка кошка сидит на коврике"
short_doc = "кошка на ковре"
long_vec = text_to_bow_vector(preprocess_text(long_doc), vocabulary)
short_vec = text_to_bow_vector(preprocess_text(short_doc), vocabulary)
sim = cosine_similarity(long_vec, short_vec)
print(f"  '{long_doc}'")
print(f"  '{short_doc}'")
print(f"  Косинус: {sim:.4f}")
print("  → Косинус спасает, но частоты всё равно искажены")

# Проблема 2: редкие и частые слова имеют одинаковый вес
print("\nПроблема 2: Редкие и частые слова одинаковы")
print("  Слово 'и' встречается в 1 из 3 документов")
print("  Слово 'сидит' встречается в 2 из 3 документов")
print("  Но в BoW они оба имеют вес 1")
print("  → Нужно учитывать редкость слова!")

# Проблема 3: размер словаря
print("\nПроблема 3: Размер словаря")
print(f"  В нашем примере словарь = {len(vocabulary)} слов")
print("  В реальном корпусе словарь может быть 100 000+ слов")
print("  → Векторы становятся очень длинными и разреженными")
print("  → Это решает TF-IDF и уменьшение размерности")

print("\nРешение проблем 1 и 2 → TF-IDF!")

