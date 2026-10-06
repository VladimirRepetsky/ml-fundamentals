"""
Практика: поиск похожих пользователей с помощью косинусного сходства.
Это основа рекомендательных систем.
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

def euclidean_distance(a, b):
    """Евклидово расстояние между двумя векторами."""
    return np.linalg.norm(a - b)

# === Данные: пользователи и их оценки фильмов ===
# Каждый пользователь — это вектор оценок для 5 фильмов
# Оценки от 1 до 5

print("=" * 60)
print("  ПОИСК ПОХОЖИХ ПОЛЬЗОВАТЕЛЕЙ")
print("=" * 60)

users = {
    "Alice":   np.array([5, 3, 4, 4, 2]),
    "Bob":     np.array([3, 1, 2, 3, 3]),
    "Charlie": np.array([4, 3, 4, 3, 5]),
    "David":   np.array([3, 3, 1, 5, 4]),
    "Eve":     np.array([1, 5, 5, 2, 1]),
}

movies = ["Фильм 1", "Фильм 2", "Фильм 3", "Фильм 4", "Фильм 5"]

print("\nОценки пользователей:")
print(f"{'Пользователь':<12}", end="")
for movie in movies:
    print(f"{movie:>10}", end="")
print()
print("-" * 62)
for name, ratings in users.items():
    print(f"{name:<12}", end="")
    for rating in ratings:
        print(f"{rating:>10}", end="")
    print()

# === Задача: найти пользователей, похожих на Alice ===
print("\n" + "=" * 60)
print("  ИЩЕМ ПОЛЬЗОВАТЕЛЕЙ, ПОХОЖИХ НА ALICE")
print("=" * 60)

target_user = "Alice"
target_ratings = users[target_user]

print(f"\nОценки {target_user}: {target_ratings}")

# Вычисляем косинусное сходство с каждым пользователем
print("\nКосинусное сходство с другими пользователями:")
similarities = {}
for name, ratings in users.items():
    if name == target_user:
        continue
    sim = cosine_similarity(target_ratings, ratings)
    similarities[name] = sim
    print(f"  {name}: {sim:.4f}")

# Сортируем по убыванию схожести
sorted_similarities = sorted(similarities.items(), key=lambda x: x[1], reverse=True)

print("\nРейтинг схожести:")
for rank, (name, sim) in enumerate(sorted_similarities, start=1):
    print(f"  {rank}. {name}: {sim:.4f}")

# === Евклидово расстояние для сравнения ===
print("\nЕвклидово расстояние (меньше = похожее):")
distances = {}
for name, ratings in users.items():
    if name == target_user:
        continue
    dist = euclidean_distance(target_ratings, ratings)
    distances[name] = dist
    print(f"  {name}: {dist:.4f}")

sorted_distances = sorted(distances.items(), key=lambda x: x[1])
print("\nРейтинг близости (по возрастанию расстояния):")
for rank, (name, dist) in enumerate(sorted_distances, start=1):
    print(f"  {rank}. {name}: {dist:.4f}")

# === Итоги ===
print("\n" + "=" * 60)
print("  ИТОГИ")
print("=" * 60)
print(f"""
Наиболее похожий пользователь на {target_user}:
  {sorted_similarities[0][0]} (косинусное сходство: {sorted_similarities[0][1]:.4f})

Это основа рекомендательных систем:
- Если {sorted_similarities[0][0]} нравится фильм, который {target_user} не смотрел,
  мы можем рекомендовать этот фильм {target_user}.

В реальных системах:
- Используются миллионы пользователей
- Векторы имеют тысячи измерений
- Используются оптимизированные библиотеки (scikit-learn, PyTorch)
""")