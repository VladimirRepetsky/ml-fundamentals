-- ============================================================
-- День 21: Агрегатные функции
-- ============================================================

-- 1. COUNT(*) — общее количество товаров
SELECT COUNT(*) AS total_products FROM products;

-- 2. COUNT с условием (через FILTER — только в PostgreSQL)
SELECT
    COUNT(*) AS total,
    COUNT(*) FILTER (WHERE price > 100) AS expensive_count,
    COUNT(*) FILTER (WHERE price <= 100) AS cheap_count
FROM products;

-- 3. SUM — общая стоимость всех товаров на складе
SELECT
    SUM(quantity) AS total_quantity,
    SUM(price * quantity) AS total_stock_value
FROM products;

-- 4. AVG — средняя цена товара
SELECT
    AVG(price) AS avg_price,
    AVG(quantity) AS avg_quantity
FROM products;

-- 5. AVG с округлением
SELECT
    ROUND(AVG(price), 2) AS avg_price_rounded,
    ROUND(AVG(quantity), 2) AS avg_quantity_rounded
FROM products;

-- 6. MIN и MAX — минимальная и максимальная цены
SELECT
    MIN(price) AS min_price,
    MAX(price) AS max_price,
    MAX(price) - MIN(price) AS price_range
FROM products;

-- 7. Все агрегаты вместе
SELECT
    COUNT(*) AS total_products,
    ROUND(AVG(price), 2) AS avg_price,
    MIN(price) AS min_price,
    MAX(price) AS max_price,
    SUM(price * quantity) AS total_stock_value
FROM products;

-- 8. COUNT(DISTINCT ...) — количество уникальных значений
SELECT
    COUNT(DISTINCT category) AS unique_categories,
    COUNT(DISTINCT name) AS unique_names
FROM products;

-- 9. Список уникальных категорий
SELECT DISTINCT category FROM products;