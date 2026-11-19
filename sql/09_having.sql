-- ============================================================
-- День 21: HAVING — фильтрация групп
-- ============================================================

-- 1. Категории, где средняя цена выше 150
-- (прямое задание из программы!)
SELECT
    category,
    ROUND(AVG(price), 2) AS avg_price
FROM products
GROUP BY category
HAVING AVG(price) > 150
ORDER BY avg_price DESC;

-- 2. Категории с количеством товаров >= 5
SELECT
    category,
    COUNT(*) AS product_count
FROM products
GROUP BY category
HAVING COUNT(*) >= 5
ORDER BY product_count DESC;

-- 3. Категории, где есть товары дороже 500
SELECT
    category,
    MAX(price) AS max_price
FROM products
GROUP BY category
HAVING MAX(price) > 500;

-- 4. Категории с общей стоимостью склада > 10000
SELECT
    category,
    SUM(price * quantity) AS stock_value
FROM products
GROUP BY category
HAVING SUM(price * quantity) > 10000
ORDER BY stock_value DESC;

-- 5. HAVING с несколькими условиями
SELECT
    category,
    COUNT(*) AS product_count,
    ROUND(AVG(price), 2) AS avg_price
FROM products
GROUP BY category
HAVING COUNT(*) >= 4 AND AVG(price) > 50
ORDER BY avg_price DESC;

-- 6. Использование алиаса в HAVING (PostgreSQL разрешает!)
SELECT
    category,
    ROUND(AVG(price), 2) AS avg_price
FROM products
GROUP BY category
HAVING ROUND(AVG(price), 2) > 100
ORDER BY avg_price DESC;