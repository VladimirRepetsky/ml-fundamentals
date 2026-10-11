"""
МИНИ-ПРОЕКТ НЕДЕЛИ 3: Полный цикл векторизации и анализа данных
=================================================================
Этот проект объединяет всю математику Недели 3:
1. Представление данных как матрицы
2. Скалярное произведение и косинусное сходство
3. Нормы вектора
4. Векторизация текста (TF-IDF)
5. Собственные значения и SVD
6. Снижение размерности
"""
import numpy as np
import re

# ============================================================
# УТИЛИТЫ
# ============================================================

def cosine_similarity(a, b):
    """Косинусное сходство между двумя векторами."""
    dot = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)

def preprocess_text(text):
    """Предобработка текста."""
    text = text.lower()
    text = re.sub(r'[^а-яёa-z0-9\s]', '', text)
    return re.sub(r'\s+', ' ', text).strip()

def text_to_words(text):
    """Разбивает текст на слова."""
    return preprocess_text(text).split()

class SimpleTfidf:
    """Упрощённый TF-IDF векторизатор."""
    
    def __init__(self):
        self.vocabulary = []
        self.word_to_index = {}
        self.idf = None
    
    def fit_transform(self, documents):
        """Строит словарь и возвращает матрицу TF-IDF."""
        # Словарь
        vocab_set = set()
        for doc in documents:
            vocab_set.update(text_to_words(doc))
        self.vocabulary = sorted(list(vocab_set))
        self.word_to_index = {w: i for i, w in enumerate(self.vocabulary)}
        
        # IDF
        n_docs = len(documents)
        self.idf = np.zeros(len(self.vocabulary))
        for i, word in enumerate(self.vocabulary):
            doc_count = sum(1 for doc in documents if word in text_to_words(doc))
            self.idf[i] = np.log((n_docs + 1) / (doc_count + 1)) + 1
        
        # TF-IDF матрица
        n_words = len(self.vocabulary)
        tfidf = np.zeros((n_docs, n_words))
        for i, doc in enumerate(documents):
            words = text_to_words(doc)
            for word in words:
                if word in self.word_to_index:
                    tfidf[i, self.word_to_index[word]] += 1
            if len(words) > 0:
                tfidf[i] /= len(words)
            tfidf[i] *= self.idf
        
        return tfidf
    
    def transform(self, documents):
        """Преобразует новые документы в векторы."""
        n_words = len(self.vocabulary)
        tfidf = np.zeros((len(documents), n_words))
        for i, doc in enumerate(documents):
            words = text_to_words(doc)
            for word in words:
                if word in self.word_to_index:
                    tfidf[i, self.word_to_index[word]] += 1
            if len(words) > 0:
                tfidf[i] /= len(words)
            tfidf[i] *= self.idf
        return tfidf

# ============================================================
# ДАННЫЕ
# ============================================================

documents = [
    "Python это язык программирования для анализа данных",
    "Машинное обучение использует алгоритмы и данные",
    "Анализ данных включает статистику и визуализацию",
    "Нейронные сети это основа глубокого обучения",
    "Глубокое обучение использует нейронные сети",
    "Статистика помогает анализировать данные",
    "Алгоритмы сортировки важны в программировании",
    "Визуализация данных помогает понимать результаты",
]

queries = [
    "машинное обучение и данные",
    "программирование на python",
    "статистика и анализ",
]

# ============================================================
# ЧАСТЬ 1: ВЕКТОРИЗАЦИЯ ТЕКСТА
# ============================================================

def part1_vectorization():
    print("\n" + "=" * 60)
    print("  ЧАСТЬ 1: ВЕКТОРИЗАЦИЯ ТЕКСТА (День 18)")
    print("=" * 60)
    
    vectorizer = SimpleTfidf()
    tfidf_matrix = vectorizer.fit_transform(documents)
    
    print(f"\nДокументов: {len(documents)}")
    print(f"Размер словаря: {len(vectorizer.vocabulary)}")
    print(f"Матрица TF-IDF: {tfidf_matrix.shape}")
    
    return vectorizer, tfidf_matrix

# ============================================================
# ЧАСТЬ 2: ПОИСК ПОХОЖИХ ДОКУМЕНТОВ
# ============================================================

def part2_search(vectorizer, tfidf_matrix):
    print("\n" + "=" * 60)
    print("  ЧАСТЬ 2: ПОИСК ПОХОЖИХ ДОКУМЕНТОВ (День 17)")
    print("=" * 60)
    
    for query in queries:
        print(f"\n🔍 Запрос: '{query}'")
        query_vec = vectorizer.transform([query])[0]
        
        similarities = []
        for i in range(len(documents)):
            sim = cosine_similarity(query_vec, tfidf_matrix[i])
            similarities.append((sim, i))
        
        similarities.sort(reverse=True)
        
        print("  Топ-3 похожих документа:")
        for rank, (sim, idx) in enumerate(similarities[:3], start=1):
            print(f"    {rank}. [{sim:.4f}] {documents[idx]}")

# ============================================================
# ЧАСТЬ 3: СОБСТВЕННЫЕ ЗНАЧЕНИЯ И НАПРАВЛЕНИЯ ДАННЫХ
# ============================================================

def part3_eigen(tfidf_matrix):
    print("\n" + "=" * 60)
    print("  ЧАСТЬ 3: СОБСТВЕННЫЕ ЗНАЧЕНИЯ (День 19)")
    print("=" * 60)
    
    # Ковариационная матрица признаков (слов)
    cov_matrix = np.cov(tfidf_matrix.T)
    
    # Обработка случая, когда ковариационная матрица содержит NaN
    cov_matrix = np.nan_to_num(cov_matrix)
    
    eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
    
    # Сортируем по убыванию
    sorted_idx = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[sorted_idx]
    eigenvectors = eigenvectors[:, sorted_idx]
    
    # Берём только вещественные части
    eigenvalues = np.real(eigenvalues)
    
    total_variance = np.sum(np.abs(eigenvalues))
    
    print(f"\nВсего признаков (слов): {len(eigenvalues)}")
    print(f"\nТоп-5 собственных значений:")
    for i in range(min(5, len(eigenvalues))):
        explained = np.abs(eigenvalues[i]) / total_variance * 100
        print(f"  λ_{i+1} = {eigenvalues[i]:.4f} → {explained:.1f}% дисперсии")
    
    return eigenvalues, eigenvectors

# ============================================================
# ЧАСТЬ 4: SVD И СНИЖЕНИЕ РАЗМЕРНОСТИ
# ============================================================

def part4_svd(tfidf_matrix):
    print("\n" + "=" * 60)
    print("  ЧАСТЬ 4: SVD И СНИЖЕНИЕ РАЗМЕРНОСТИ (День 19)")
    print("=" * 60)
    
    # SVD матрицы TF-IDF
    U, s, Vt = np.linalg.svd(tfidf_matrix, full_matrices=False)
    
    print(f"\nСингулярные числа: {s.round(4)}")
    
    # Доля объяснённой дисперсии
    total = np.sum(s ** 2)
    print(f"\nДоля объяснённой дисперсии:")
    cumulative = 0
    for i, sv in enumerate(s):
        explained = sv ** 2 / total * 100
        cumulative += explained
        print(f"  Компонента {i+1}: {explained:>5.1f}% (накопительно: {cumulative:>5.1f}%)")
    
    # Выбираем k для 90% дисперсии
    target = 0.90
    cumulative = 0
    k = 0
    for i, sv in enumerate(s):
        cumulative += sv ** 2 / total
        if cumulative >= target:
            k = i + 1
            break
    
    print(f"\nДля сохранения {target*100:.0f}% дисперсии нужно k={k}")
    
    # Проекция на первые k компонент
    V_k = Vt[:k, :].T
    projected = tfidf_matrix @ V_k
    
    print(f"\nРазмерность снижена: {tfidf_matrix.shape[1]} → {projected.shape[1]}")
    print(f"Форма спроецированных данных: {projected.shape}")
    
    # === Поиск похожих документов в сниженном пространстве ===
    print("\n=== Поиск в сниженном пространстве ===")
    for i, doc in enumerate(documents[:3]):
        print(f"\nДокумент: '{doc}'")
        sims = []
        for j in range(len(projected)):
            if i != j:
                sim = cosine_similarity(projected[i], projected[j])
                sims.append((sim, j))
        sims.sort(reverse=True)
        print(f"  Наиболее похожий: [{sims[0][0]:.4f}] {documents[sims[0][1]]}")
    
    return U, s, Vt, k

# ============================================================
# ЧАСТЬ 5: СРАВНЕНИЕ ПОЛНОГО И СНИЖЕННОГО ПРОСТРАНСТВА
# ============================================================

def part5_comparison(tfidf_matrix, projected):
    print("\n" + "=" * 60)
    print("  ЧАСТЬ 5: СРАВНЕНИЕ ПРОСТРАНСТВ")
    print("=" * 60)
    
    print(f"\nПолное пространство: {tfidf_matrix.shape[1]} измерений")
    print(f"Сниженное пространство: {projected.shape[1]} измерений")
    
    # Считаем матрицы сходства в обоих пространствах
    n = len(documents)
    sim_full = np.zeros((n, n))
    sim_reduced = np.zeros((n, n))
    
    for i in range(n):
        for j in range(n):
            sim_full[i, j] = cosine_similarity(tfidf_matrix[i], tfidf_matrix[j])
            sim_reduced[i, j] = cosine_similarity(projected[i], projected[j])
    
    # Сравниваем: насколько похожи матрицы сходства
    # Берём только верхний треугольник (без диагонали)
    mask = np.triu(np.ones((n, n), dtype=bool), k=1)
    diff = np.abs(sim_full[mask] - sim_reduced[mask])
    
    print(f"\nСредняя разница в косинусном сходстве: {np.mean(diff):.4f}")
    print(f"Максимальная разница: {np.max(diff):.4f}")
    
    if np.mean(diff) < 0.1:
        print("✅ Снижение размерности сохранило структуру сходства!")
    else:
        print("⚠️ Снижение размерности значительно изменило сходство.")

# ============================================================
# ИТОГИ
# ============================================================

def final_summary():
    print("\n" + "=" * 60)
    print("  ИТОГИ НЕДЕЛИ 3")
    print("=" * 60)
    print("""
╔══════════════════════════════════════════════════════════╗
║           НЕДЕЛЯ 3: МАТЕМАТИКА ДЛЯ ML                   ║
║        Линейная алгебра и векторное представление       ║
╚══════════════════════════════════════════════════════════╝

✅ День 14: Матрицы и линейная алгебра в NumPy
   - Транспонирование, матричное умножение
   - Агрегации по осям
   - Евклидово расстояние

✅ День 17: Геометрия векторов
   - Скалярное произведение: A·B = |A|·|B|·cos(θ)
   - Нормы: L1, L2, L∞
   - Косинусное сходство
   - Поиск похожих пользователей

✅ День 18: Векторизация текста
   - Bag of Words
   - TF-IDF = TF × IDF
   - Мини-поисковик на косинусном сходстве

✅ День 19: Продвинутая линейная алгебра
   - Собственные значения: A·v = λ·v
   - Ковариационная матрица и главные направления
   - SVD: A = U·Σ·Vᵀ
   - Снижение размерности
   - Сжатие данных

╔══════════════════════════════════════════════════════════╗
║              ПРАКТИЧЕСКИЕ ЗАДАНИЯ НЕДЕЛИ 3              ║
╚══════════════════════════════════════════════════════════╝

✅ Данные представлены как матрица признаков
✅ Транспонирование матрицы
✅ Среднее значение по столбцам
✅ Матричное умножение X.T @ X
✅ Евклидово расстояние
✅ Векторизация текста
✅ Понимание собственных значений и SVD

╔══════════════════════════════════════════════════════════╗
║              СВЯЗЬ С БУДУЩИМИ ПРОЕКТАМИ                 ║
╚══════════════════════════════════════════════════════════╝

📌 Неделя 10: Проект KNN
   → Евклидово расстояние (День 14)
   → Косинусное сходство (День 17)

📌 Будущие рекомендательные системы
   → Косинусное сходство (День 17)
   → SVD (День 19)

📌 Будущие NLP-задачи
   → Векторизация текста (День 18)
   → Латентно-семантический анализ через SVD (День 19)

📌 Будущий PCA и снижение размерности
   → Собственные значения (День 19)
   → Ковариационная матрица (День 19)
""")

# ============================================================
# ЗАПУСК
# ============================================================

if __name__ == "__main__":
    print("\n" + "█" * 60)
    print("  МИНИ-ПРОЕКТ НЕДЕЛИ 3")
    print("  Полный цикл векторизации и анализа данных")
    print("█" * 60)
    
    # Часть 1: Векторизация
    vectorizer, tfidf_matrix = part1_vectorization()
    
    # Часть 2: Поиск
    part2_search(vectorizer, tfidf_matrix)
    
    # Часть 3: Собственные значения
    part3_eigen(tfidf_matrix)
    
    # Часть 4: SVD и снижение размерности
    U, s, Vt, k = part4_svd(tfidf_matrix)
    
    # Проекция для сравнения
    V_k = Vt[:k, :].T
    projected = tfidf_matrix @ V_k
    
    # Часть 5: Сравнение
    part5_comparison(tfidf_matrix, projected)
    
    # Итоги
    final_summary()
    
    print("\n" + "=" * 60)
    print("  НЕДЕЛЯ 3 ЗАВЕРШЕНА! 🎉")
    print("=" * 60 + "\n")