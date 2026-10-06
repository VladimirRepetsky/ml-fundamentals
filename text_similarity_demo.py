"""
Практика: поиск похожих текстов с помощью косинусного сходства.
Это основа поисковых систем и NLP.

Используем упрощённую модель "Мешок слов" (Bag of Words):
каждый текст представляется как вектор частот слов.
"""
import numpy as np

def cosine_similarity(a, b):
    """Косинусное сходство между двумя векторами."""
    dot = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)

def text_to_words(text):
    """Разбивает текст на слова, убирает пунктуацию и приводит к нижнему регистру."""
    punctuation = ".,!?;:()\"'«»-"
    for char in punctuation:
        text = text.replace(char, "")
    return text.lower().split()

def build_vocabulary(texts):
    """Строит словарь всех уникальных слов из текстов."""
    vocab = set()
    for text in texts:
        words = text_to_words(text)
        vocab.update(words)
    return sorted(list(vocab))

def text_to_vector(text, vocabulary):
    """
    Преобразует текст в вектор частот слов (Bag of Words).
    Каждая координата вектора — частота соответствующего слова из словаря.
    """
    words = text_to_words(text)
    vector = np.zeros(len(vocabulary))
    for word in words:
        if word in vocabulary:
            index = vocabulary.index(word)
            vector[index] += 1
    return vector

# === Данные: несколько коротких текстов ===
documents = [
    "Python это язык программирования",
    "Python используется в машинном обучении",
    "Машинное обучение использует алгоритмы",
    "Кошки и собаки это домашние животные",
    "Собаки любят играть с мячом",
    "Я люблю программировать на Python",
]

print("=" * 60)
print("  ПОИСК ПОХОЖИХ ТЕКСТОВ")
print("=" * 60)

print("\nДокументы:")
for i, doc in enumerate(documents):
    print(f"  {i+1}. {doc}")

# === Шаг 1: строим словарь ===
vocabulary = build_vocabulary(documents)
print(f"\nСловарь ({len(vocabulary)} уникальных слов):")
print(vocabulary)

# === Шаг 2: преобразуем тексты в векторы ===
print("\nВекторное представление документов:")
vectors = []
for doc in documents:
    vector = text_to_vector(doc, vocabulary)
    vectors.append(vector)
    print(f"  '{doc}'")
    print(f"    → {vector.astype(int)}")

vectors = np.array(vectors)

# === Шаг 3: вычисляем матрицу косинусных сходств ===
print("\nМатрица косинусных сходств:")
similarity_matrix = np.zeros((len(documents), len(documents)))
for i in range(len(documents)):
    for j in range(len(documents)):
        similarity_matrix[i, j] = cosine_similarity(vectors[i], vectors[j])

# Печатаем матрицу
print(f"\n{'':>3}", end="")
for j in range(len(documents)):
    print(f"  doc{j+1}", end="")
print()
for i in range(len(documents)):
    print(f"doc{i+1}", end="")
    for j in range(len(documents)):
        print(f" {similarity_matrix[i, j]:.2f}", end="")
    print()

# === Шаг 4: находим похожие документы ===
print("\n" + "=" * 60)
print("  ПОИСК ПОХОЖИХ ДОКУМЕНТОВ")
print("=" * 60)

query = "Python программирование"
print(f"\nЗапрос: '{query}'")

query_vector = text_to_vector(query, vocabulary)
print(f"Вектор запроса: {query_vector.astype(int)}")

# Вычисляем сходство запроса с каждым документом
similarities = []
for i, doc in enumerate(documents):
    sim = cosine_similarity(query_vector, vectors[i])
    similarities.append((sim, i, doc))

# Сортируем по убыванию схожести
similarities.sort(reverse=True)

print("\nРезультаты поиска:")
for rank, (sim, idx, doc) in enumerate(similarities[:3], start=1):
    print(f"  {rank}. [{sim:.4f}] {doc}")

# === Итоги ===
print("\n" + "=" * 60)
print("  ИТОГИ")
print("=" * 60)
print("""
Только что ыла реализована упрощённая поисковая система.

Это работает так:
1. Каждый текст представляется как вектор частот слов.
2. Запрос тоже представляется как вектор.
3. Косинусное сходство находит ближайшие документы.

В реальных поисковых системах:
- Используются миллионы документов
- Используются более продвинутые методы (TF-IDF, эмбеддинги)
- Используются нейросетевые модели (BERT, GPT)

Но базовая идея та же: векторы и косинусное сходство.

В День 18 будет TF-IDF — более продвинутый способ
векторизации текста.
""")