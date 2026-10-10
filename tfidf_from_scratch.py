"""
Реализация TF-IDF с нуля на NumPy.
Это один из ключевых алгоритмов для работы с текстом в ML.
"""
import numpy as np
import re

# ============================================================
# УТИЛИТЫ
# ============================================================

def preprocess_text(text):
    """Предобработка текста."""
    text = text.lower()
    text = re.sub(r'[^а-яёa-z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def text_to_words(text):
    """Разбивает текст на слова."""
    return text.split()

# ============================================================
# TF-IDF С НУЛЯ
# ============================================================

class TfidfVectorizer:
    """
    Векторизатор текста методом TF-IDF.
    Реализация с нуля на NumPy.
    """
    
    def __init__(self):
        self.vocabulary = []          # список слов
        self.word_to_index = {}       # слово → индекс
        self.idf = None               # вектор IDF
    
    def fit(self, documents):
        """
        Строит словарь и вычисляет IDF.
        Параметры:
            documents: список строк (документов)
        """
        # 1. Предобработка
        processed = [preprocess_text(doc) for doc in documents]
        
        # 2. Построение словаря
        vocab_set = set()
        for doc in processed:
            words = text_to_words(doc)
            vocab_set.update(words)
        self.vocabulary = sorted(list(vocab_set))
        self.word_to_index = {word: i for i, word in enumerate(self.vocabulary)}
        
        # 3. Вычисление IDF
        n_docs = len(processed)
        self.idf = np.zeros(len(self.vocabulary))
        for i, word in enumerate(self.vocabulary):
            doc_count = sum(
                1 for doc in processed
                if word in text_to_words(doc)
            )
            # Сглаживание: log((N + 1) / (df + 1)) + 1
            self.idf[i] = np.log((n_docs + 1) / (doc_count + 1)) + 1
        
        return self
    
    def transform(self, documents):
        """
        Преобразует документы в матрицу TF-IDF.
        Параметры:
            documents: список строк
        Возвращает:
            матрица (n_documents × n_words)
        """
        processed = [preprocess_text(doc) for doc in documents]
        n_docs = len(processed)
        n_words = len(self.vocabulary)
        tfidf_matrix = np.zeros((n_docs, n_words))
        
        for i, doc in enumerate(processed):
            words = text_to_words(doc)
            total_words = len(words)
            if total_words == 0:
                continue
            # TF: частота каждого слова
            for word in words:
                if word in self.word_to_index:
                    idx = self.word_to_index[word]
                    tfidf_matrix[i, idx] += 1
            # Нормализация TF
            tfidf_matrix[i] = tfidf_matrix[i] / total_words
            # Умножение на IDF
            tfidf_matrix[i] = tfidf_matrix[i] * self.idf
        
        return tfidf_matrix
    
    def fit_transform(self, documents):
        """Объединяет fit и transform."""
        self.fit(documents)
        return self.transform(documents)

# ============================================================
# ТЕСТИРОВАНИЕ
# ============================================================

print("=" * 60)
print("  TF-IDF С НУЛЯ")
print("=" * 60)

documents = [
    "Кошка сидит на коврике",
    "Собака сидит на полу",
    "Кошка и собака друзья",
]

# Создаём векторизатор
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

print(f"\nСловарь ({len(vectorizer.vocabulary)} слов):")
print(vectorizer.vocabulary)

print(f"\nIDF-вектор:")
for word, idf_val in zip(vectorizer.vocabulary, vectorizer.idf):
    print(f"  '{word}': {idf_val:.4f}")

print(f"\nМатрица TF-IDF:")
print(np.round(tfidf_matrix, 4))
print(f"Форма: {tfidf_matrix.shape}")

# === Интерпретация ===
print(f"\n=== Интерпретация ===")
print("Каждая строка — документ, каждый столбец — слово.")
print("Значение = TF × IDF.")
print("Высокое значение = слово важно для этого документа.")
print("Низкое значение = слово не важно или редко.")

# === Поиск похожего документа ===
def cosine_similarity(a, b):
    dot = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)

print(f"\n=== Поиск похожего документа ===")
query = "кошка на коврике"
query_vector = vectorizer.transform([query])[0]
print(f"Запрос: '{query}'")
print(f"Вектор запроса: {np.round(query_vector, 4)}")
print(f"\nКосинусное сходство:")
similarities = []
for i, doc in enumerate(documents):
    sim = cosine_similarity(query_vector, tfidf_matrix[i])
    similarities.append(sim)
    print(f"  Документ {i+1}: {sim:.4f} — '{doc}'")

best_idx = np.argmax(similarities)
print(f"\n✅ Наиболее похожий документ: Документ {best_idx + 1}")
print(f"   '{documents[best_idx]}'")