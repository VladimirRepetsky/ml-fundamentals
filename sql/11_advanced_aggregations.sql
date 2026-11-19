-- ============================================================
-- День 21: Продвинутые агрегации
-- ============================================================

-- 1. Условные агрегации через CASE WHEN
-- Аналог FILTER, но работает во всех СУБД
SELECT
    category,
    COUNT(*) AS total,
    SUM(CASE WHEN price < 50 THEN 1 ELSE 0 END) AS cheap_count,
    SUM(CASE WHEN price >= 50 AND price < 200 THEN 1 ELSE 0 END) AS medium_count,
    SUM(CASE WHEN price >= 200 THEN 1 ELSE 0 END) AS expensive_count
FROM products
GROUP BY category
ORDER BY category;

-- 2. Доля дорогих товаров в каждой категории
SELECT
    category,
    COUNT(*) AS total,
    SUM(CASE WHEN price > 100 THEN 1 ELSE 0 END) AS expensive,
    ROUND(
        SUM(CASE WHEN price > 100 THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS expensive_percent
FROM products
GROUP BY category
ORDER BY expensive_percent DESC;

-- 3. Самая дорогая и самая дешёвая категории
-- Подзапрос для глобального максимума
WITH category_stats AS (
    SELECT
        category,
        ROUND(AVG(price), 2) AS avg_price,
        COUNT(*) AS count
    FROM products
    GROUP BY category
)
SELECT
    category,
    avg_price,
    count,
    CASE
        WHEN avg_price = (SELECT MAX(avg_price) FROM category_stats) THEN 'Самая дорогая'
        WHEN avg_price = (SELECT MIN(avg_price) FROM category_stats) THEN 'Самая дешёвая'
        ELSE 'Средняя'
    END AS status
FROM category_stats
ORDER BY avg_price DESC;

-- 4. Категории с разбросом цен (MAX - MIN)
SELECT
    category,
    MIN(price) AS min_price,
    MAX(price) AS max_price,
    MAX(price) - MIN(price) AS price_spread,
    ROUND(AVG(price), 2) AS avg_price
FROM products
GROUP BY category
ORDER BY price_spread DESC;

-- 5. Топ-1 товар в каждой категории по цене
-- (Использование DISTINCT ON — только PostgreSQL)
SELECT DISTINCT ON (category)
    category,
    name,
    price
FROM products
ORDER BY category, price DESC;

-- 6. Статистика по ценовым сегментам
SELECT
    CASE
        WHEN price < 30 THEN '0-30'
        WHEN price < 100 THEN '30-100'
        WHEN price < 500 THEN '100-500'
        ELSE '500+'
    END AS price_segment,
    COUNT(*) AS count,
    ROUND(AVG(price), 2) AS avg_price,
    SUM(quantity) AS total_quantity
FROM products
GROUP BY price_segment
ORDER BY MIN(price);