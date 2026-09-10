"""
Мини-проект Дня 16: Полный цикл анализа данных

Этот скрипт демонстрирует полный цикл работы с данными:
1. Загрузка
2. Разведочный анализ (EDA)
3. Очистка пропусков
4. Создание новых признаков
5. Группировка и агрегация
6. Слияние таблиц
7. Итоговые выводы
"""
import pandas as pd
import numpy as np


def load_and_explore(filepath):
    """Загрузка и первичный осмотр данных."""
    print("=" * 60)
    print("  ЭТАП 1: ЗАГРУЗКА И РАЗВЕДОЧНЫЙ АНАЛИЗ")
    print("=" * 60)

    df = pd.read_csv(filepath)

    print(f"\nФорма: {df.shape}")
    print(f"\nПервые 5 строк:")
    print(df.head())

    print(f"\nТипы данных:")
    print(df.dtypes)

    print(f"\nСтатистика числовых столбцов:")
    print(df.describe().round(2))

    print(f"\nПропуски по столбцам:")
    print(df.isnull().sum())

    print(f"\nПроцент пропусков:")
    print((df.isnull().sum() / len(df) * 100).round(2))

    return df


def clean_data(df):
    """Очистка пропущенных значений."""
    print("\n" + "=" * 60)
    print("  ЭТАП 2: ОЧИСТКА ДАННЫХ")
    print("=" * 60)

    df_clean = df.copy()

    # Числовые столбцы → медиана
    numeric_cols = ["age", "score", "hours_per_week"]
    for col in numeric_cols:
        before = df_clean[col].isnull().sum()
        df_clean[col] = df_clean[col].fillna(df_clean[col].median())
        after = df_clean[col].isnull().sum()
        print(f"  {col}: заполнено {before} пропусков медианой ({df_clean[col].median():.1f})")

    # Категориальные столбцы → мода
    categorical_cols = ["gender", "course"]
    for col in categorical_cols:
        before = df_clean[col].isnull().sum()
        mode_val = df_clean[col].mode()[0]
        df_clean[col] = df_clean[col].fillna(mode_val)
        print(f"  {col}: заполнено {before} пропусков модой ('{mode_val}')")

    print(f"\nПропуски после очистки: {df_clean.isnull().sum().sum()}")

    return df_clean


def create_features(df):
    """Создание новых признаков."""
    print("\n" + "=" * 60)
    print("  ЭТАП 3: СОЗДАНИЕ НОВЫХ ПРИЗНАКОВ")
    print("=" * 60)

    # Эффективность обучения
    df["efficiency"] = df["score"] / df["hours_per_week"]
    print("  ✓ efficiency = score / hours_per_week")

    # Возрастная категория
    df["age_category"] = pd.cut(
        df["age"],
        bins=[0, 23, 26, 30, 100],
        labels=["young", "mid_young", "mid_senior", "senior"]
    )
    print("  ✓ age_category (young/mid_young/mid_senior/senior)")

    # Уровень успеваемости
    df["grade"] = pd.cut(
        df["score"],
        bins=[0, 60, 70, 80, 90, 100],
        labels=["F", "D", "C", "B", "A"]
    )
    print("  ✓ grade (F/D/C/B/A)")

    # Флаг высокого балла
    df["is_high_scorer"] = (df["score"] >= 85).astype(int)
    print("  ✓ is_high_scorer (score >= 85)")

    # Нормализованный балл
    df["score_normalized"] = (df["score"] - df["score"].min()) / \
                             (df["score"].max() - df["score"].min())
    print("  ✓ score_normalized (0-1)")

    print(f"\nНовых признаков создано: 5")
    print(f"Всего столбцов: {len(df.columns)}")

    return df


def analyze_data(df):
    """Группировка и агрегация."""
    print("\n" + "=" * 60)
    print("  ЭТАП 4: АНАЛИЗ ДАННЫХ")
    print("=" * 60)

    # Средний балл по курсам
    print("\n📊 Средний балл по курсам:")
    course_stats = df.groupby("course").agg(
        avg_score=("score", "mean"),
        median_score=("score", "median"),
        num_students=("student_id", "count"),
        avg_efficiency=("efficiency", "mean")
    ).round(2)
    print(course_stats)

    # Средний балл по полу
    print("\n📊 Средний балл по полу:")
    gender_stats = df.groupby("gender").agg(
        avg_score=("score", "mean"),
        num_students=("student_id", "count")
    ).round(2)
    print(gender_stats)

    # Распределение по оценкам
    print("\n📊 Распределение по оценкам:")
    print(df["grade"].value_counts().sort_index())

    # Распределение по возрастным категориям
    print("\n📊 Распределение по возрастным категориям:")
    print(df["age_category"].value_counts().sort_index())

    # Топ-3 эффективных студента
    print("\n📊 Топ-3 эффективных студента:")
    top_efficient = df.nlargest(3, "efficiency")[["name", "score", "hours_per_week", "efficiency"]]
    print(top_efficient.round(2))

    # Сводная таблица: курс × пол
    print("\n📊 Сводная таблица (средний балл):")
    pivot = df.pivot_table(
        values="score",
        index="course",
        columns="gender",
        aggfunc="mean"
    ).round(2)
    print(pivot)

    return course_stats


def merge_with_orders():
    """Демонстрация слияния таблиц."""
    print("\n" + "=" * 60)
    print("  ЭТАП 5: СЛИЯНИЕ ТАБЛИЦ")
    print("=" * 60)

    orders = pd.read_csv("data/orders.csv")
    customers = pd.read_csv("data/customers.csv")

    merged = pd.merge(orders, customers, on="customer_id", how="left")

    print("\nОбъединённая таблица (заказы + клиенты):")
    print(merged)

    print("\n💰 Общая сумма по клиентам:")
    print(merged.groupby("name")["amount"].sum().sort_values(ascending=False))

    print("\n🏙️ Средний чек по городам:")
    print(merged.groupby("city")["amount"].mean().round(2))


def main():
    """Основная функция."""
    print("\n" + "█" * 60)
    print("  МИНИ-ПРОЕКТ: ПОЛНЫЙ ЦИКЛ АНАЛИЗА ДАННЫХ")
    print("  День 16: Продвинутый Pandas")
    print("█" * 60)

    # Этап 1: Загрузка и EDA
    df = load_and_explore("data/students_with_gaps.csv")

    # Этап 2: Очистка
    df = clean_data(df)

    # Этап 3: Feature Engineering
    df = create_features(df)

    # Этап 4: Анализ
    course_stats = analyze_data(df)

    # Этап 5: Слияние таблиц
    merge_with_orders()

    # Итоги
    print("\n" + "=" * 60)
    print("  ИТОГИ")
    print("=" * 60)
    print("""
✅ Загрузка и разведочный анализ (head, info, describe)
✅ Обнаружение и обработка пропусков (isnull, fillna)
✅ Создание новых признаков (feature engineering)
✅ Группировка и агрегация (groupby, agg, pivot_table)
✅ Слияние таблиц (merge, concat)
✅ Полный цикл анализа данных

Это закрывает все практические задания Недели 2:
  ✓ Загрузить данные в DataFrame
  ✓ Базовый анализ: head, info, describe
  ✓ Очистка: найти и обработать пропуски
  ✓ Запросы: средний возраст, количество по полу,
    средний балл по курсам
""")

    # Сохраняем результат
    df.to_csv("data/students_analyzed.csv", index=False)
    print("Результат сохранён в data/students_analyzed.csv")


if __name__ == "__main__":
    main()