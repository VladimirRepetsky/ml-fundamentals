-- ============================================================
-- День 21: GROUP BY — группировка данных
-- ============================================================

-- 1. Количество товаров по каждой категории
SELECT category, COUNT(*) AS product_count
FROM products
GROUP BY category;

-- 2. Сортировка результата группировки
SELECT category, COUNT(*) AS product_count
FROM products
GROUP BY category
ORDER BY product_count DESC;

-- 3. Несколько агрегаций для каждой группы
SELECT
    category,
    COUNT(*) AS product_count,
    ROUND(AVG(price), 2) AS avg_price,
    MIN(price) AS min_price,
    MAX(price) AS max_price,
    SUM(quantity) AS total_quantity
FROM products
GROUP BY category
ORDER BY avg_price DESC;

-- 4. Суммарная стоимость товаров на складе по категориям
SELECT
    category,
    COUNT(*) AS product_count,
    SUM(price * quantity) AS stock_value
FROM products
GROUP BY category
ORDER BY stock_value DESC;

-- 5. Процент товаров в каждой категории от общего количества
SELECT
    category,
    COUNT(*) AS count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM products), 2) AS percentage
FROM products
GROUP BY category
ORDER BY count DESC;

-- 6. GROUP BY с несколькими столбцами
-- Сколько товаров каждого типа в каждой категории?
SELECT
    category,
    CASE
        WHEN price < 50 THEN 'Дешёвые'
        WHEN price < 200 THEN 'Средние'
        ELSE 'Дорогие'
    END AS price_segment,
    COUNT(*) AS count
FROM products
GROUP BY category, price_segment
ORDER BY category, price_segment;