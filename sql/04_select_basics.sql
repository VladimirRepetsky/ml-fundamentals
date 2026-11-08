-- ============================================================
-- День 20: Базовый SELECT
-- ============================================================

-- 1. Получить ВСЕ товары и ВСЕ столбцы
SELECT * FROM products;

-- 2. Получить только определённые столбцы
SELECT name, category, price FROM products;

-- 3. Получить уникальные категории
SELECT DISTINCT category FROM products;

-- 4. Получить количество товаров
SELECT COUNT(*) AS total_products FROM products;

-- 5. Получить первый товар
SELECT * FROM products LIMIT 1;

-- 6. Получить товары с вычисляемым столбцом
SELECT
    name,
    price,
    quantity,
    price * quantity AS total_value
FROM products;

-- 7. Переименование столбцов в результате (алиасы)
SELECT
    name AS "Название товара",
    category AS "Категория",
    price AS "Цена, руб."
FROM products;

-- 8. Выборка с вычислением
SELECT
    name,
    price,
    price * 0.9 AS price_with_discount
FROM products;

-- 9. Фильтр через WHERE с условием (введение, подробнее в следующем шаге)
SELECT name, price FROM products WHERE price > 500;

-- 10. Получить все категории и количество товаров в каждой (введение в GROUP BY)
SELECT category, COUNT(*) AS product_count
FROM products
GROUP BY category
ORDER BY product_count DESC;