-- ============================================================
-- День 21: Практические задания из программы
-- ============================================================
-- Эти задания закрывают требования Недели 4 (часть 2):
-- ✓ Посчитать общее количество товаров по каждой категории
-- ✓ Найти категории, где средняя цена выше 150
-- ✓ Вычислить суммарную стоимость товаров по категориям
-- ✓ Найти категорию с максимальным количеством товаров
-- ✓ Найти категории, где есть товары дороже 500
-- ============================================================

-- ============================================================
-- Задание 1: Общее количество товаров по каждой категории
-- ============================================================
SELECT
    category,
    COUNT(*) AS product_count
FROM products
GROUP BY category
ORDER BY product_count DESC;

-- ============================================================
-- Задание 2: Категории, где средняя цена выше 150
-- ============================================================
SELECT
    category,
    ROUND(AVG(price), 2) AS avg_price
FROM products
GROUP BY category
HAVING AVG(price) > 150
ORDER BY avg_price DESC;

-- ============================================================
-- Задание 3: Суммарная стоимость товаров по категориям
-- (с учётом количества на складе)
-- ============================================================
SELECT
    category,
    COUNT(*) AS product_count,
    SUM(quantity) AS total_quantity,
    SUM(price * quantity) AS total_stock_value
FROM products
GROUP BY category
ORDER BY total_stock_value DESC;

-- ============================================================
-- Задание 4: Категория с максимальным количеством товаров
-- ============================================================
SELECT
    category,
    COUNT(*) AS product_count
FROM products
GROUP BY category
ORDER BY product_count DESC
LIMIT 1;

-- Альтернативный вариант через подзапрос
SELECT category, COUNT(*) AS product_count
FROM products
GROUP BY category
HAVING COUNT(*) = (
    SELECT MAX(cnt)
    FROM (
        SELECT COUNT(*) AS cnt
        FROM products
        GROUP BY category
    ) AS counts
);

-- ============================================================
-- Задание 5: Категории, где есть товары дороже 500
-- ============================================================
SELECT
    category,
    MAX(price) AS max_price,
    COUNT(*) AS total_products
FROM products
GROUP BY category
HAVING MAX(price) > 500
ORDER BY max_price DESC;

-- Альтернатива без HAVING (через подзапрос с IN)
SELECT DISTINCT category
FROM products
WHERE category IN (
    SELECT category
    FROM products
    WHERE price > 500
);

-- ============================================================
-- Дополнительные задания для закрепления
-- ============================================================

-- Задание 6: Полная статистика по категориям
SELECT
    category,
    COUNT(*) AS count,
    ROUND(AVG(price), 2) AS avg_price,
    ROUND(AVG(quantity), 2) AS avg_quantity,
    MIN(price) AS min_price,
    MAX(price) AS max_price,
    SUM(price * quantity) AS stock_value
FROM products
GROUP BY category
ORDER BY stock_value DESC;

-- Задание 7: Категории с товарами в разных ценовых сегментах
SELECT
    category,
    SUM(CASE WHEN price < 50 THEN 1 ELSE 0 END) AS cheap,
    SUM(CASE WHEN price BETWEEN 50 AND 200 THEN 1 ELSE 0 END) AS medium,
    SUM(CASE WHEN price > 200 THEN 1 ELSE 0 END) AS expensive,
    COUNT(*) AS total
FROM products
GROUP BY category
ORDER BY category;

-- Задание 8: Категории с высокой средней ценой И большим ассортиментом
SELECT
    category,
    COUNT(*) AS count,
    ROUND(AVG(price), 2) AS avg_price
FROM products
GROUP BY category
HAVING AVG(price) > 100 AND COUNT(*) >= 5
ORDER BY avg_price DESC;

-- Задание 9: Сколько товаров дешевле средней цены по категории
WITH category_avg AS (
    SELECT category, AVG(price) AS avg_price
    FROM products
    GROUP BY category
)
SELECT
    p.category,
    COUNT(*) AS below_avg_count,
    ROUND(ca.avg_price, 2) AS category_avg
FROM products p
JOIN category_avg ca ON p.category = ca.category
WHERE p.price < ca.avg_price
GROUP BY p.category, ca.avg_price
ORDER BY below_avg_count DESC;