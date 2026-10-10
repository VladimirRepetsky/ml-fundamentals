"""
Мини-поисковик на TF-IDF + косинусное сходство.
Это упрощённая версия того, как работают поисковые системы.
"""
import numpy as np
import re

class MiniSearchEngine:
    """
    Мини-поисковик на основе TF-IDF.
    """
    
    def __init__(self):
        self.documents = []
        self.vocabulary = []
        self.word_to_index = {}
        self.idf = None
        self.tfidf_matrix = None
    
    def preprocess(self, text):
        text = text.lower()
        text = re.sub(r'[^а-яёa-z0-9\s]', '', text)
        return re.sub(r'\s+', ' ', text).strip()
    
    def tokenize(self, text):
        return self.preprocess(text).split()
    
    def index_documents(self, documents):
        """Индексирует коллекцию документов."""
        self.documents = documents
        n_docs = len(documents)
        
        # Словарь
        vocab_set = set()
        for doc in documents:
            vocab_set.update(self.tokenize(doc))
        self.vocabulary = sorted(list(vocab_set))
        self.word_to_index = {w: i for i, w in enumerate(self.vocabulary)}
        
        # IDF
        self.idf = np.zeros(len(self.vocabulary))
        for i, word in enumerate(self.vocabulary):
            doc_count = sum(1 for doc in documents if word in self.tokenize(doc))
            self.idf[i] = np.log((n_docs + 1) / (doc_count + 1)) + 1
        
        # TF-IDF матрица
        self.tfidf_matrix = np.zeros((n_docs, len(self.vocabulary)))
        for i, doc in enumerate(documents):
            words = self.tokenize(doc)
            for word in words:
                if word in self.word_to_index:
                    self.tfidf_matrix[i, self.word_to_index[word]] += 1
            if len(words) > 0:
                self.tfidf_matrix[i] /= len(words)
            self.tfidf_matrix[i] *= self.idf
        
        print(f"Индексировано {n_docs} документов.")
        print(f"Размер словаря: {len(self.vocabulary)} слов.")
    
    def _vectorize(self, text):
        """Векторизует один текст."""
        words = self.tokenize(text)
        vec = np.zeros(len(self.vocabulary))
        for word in words:
            if word in self.word_to_index:
                vec[self.word_to_index[word]] += 1
        if len(words) > 0:
            vec /= len(words)
        vec *= self.idf
        return vec
    
    def _cosine_similarity(self, a, b):
        dot = np.dot(a, b)
        norm_a = np.linalg.norm(a)
        norm_b = np.linalg.norm(b)
        if norm_a == 0 or norm_b == 0:
            return 0.0
        return dot / (norm_a * norm_b)
    
    def search(self, query, top_k=3):
        """
        Ищет наиболее похожие документы на запрос.
        Возвращает топ-k результатов.
        """
        query_vec = self._vectorize(query)
        
        similarities = []
        for i in range(len(self.documents)):
            sim = self._cosine_similarity(query_vec, self.tfidf_matrix[i])
            similarities.append((sim, i))
        
        # Сортируем по убыванию схожести
        similarities.sort(reverse=True)
        
        results = []
        for sim, idx in similarities[:top_k]:
            results.append({
                "rank": len(results) + 1,
                "document": self.documents[idx],
                "similarity": round(sim, 4),
                "doc_id": idx
            })
        
        return results

# ============================================================
# ТЕСТИРОВАНИЕ
# ============================================================

print("=" * 60)
print("  МИНИ-ПОИСКОВИК НА TF-IDF")
print("=" * 60)

# Коллекция документов (имитация базы знаний)
documents = [
    "Python это язык программирования для анализа данных",
    "Машинное обучение использует алгоритмы для предсказания",
    "Анализ данных включает статистику и визуализацию",
    "Нейронные сети это основа глубокого обучения",
    "Python используется в машинном обучении и анализе данных",
    "Алгоритмы сортировки и поиска важны в программировании",
    "Глубокое обучение использует нейронные сети с множеством слоёв",
    "Статистика помогает принимать решения на основе данных",
]

# Создаём поисковик
engine = MiniSearchEngine()
engine.index_documents(documents)

# Поисковые запросы
queries = [
    "язык программирования Python",
    "нейронные сети и глубокое обучение",
    "статистика и анализ данных",
    "алгоритмы для предсказания",
]

print()
for query in queries:
    print(f"\n🔍 Запрос: '{query}'")
    results = engine.search(query, top_k=3)
    for r in results:
        print(f"  {r['rank']}. [{r['similarity']:.4f}] {r['document']}")
    print()

# Интерактивный режим
print("=" * 60)
print("  ИНТЕРАКТИВНЫЙ ПОИСК")
print("=" * 60)
print("Введите 'выход' для завершения.\n")

while True:
    query = input("Введите запрос: ").strip()
    if query.lower() == "выход":
        print("До свидания!")
        break
    if query == "":
        continue
    results = engine.search(query, top_k=3)
    print(f"\nРезультаты для '{query}':")
    for r in results:
        print(f"  {r['rank']}. [{r['similarity']:.4f}] {r['document']}")
    print()