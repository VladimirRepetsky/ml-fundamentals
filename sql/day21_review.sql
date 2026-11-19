-- ============================================================
-- День 21: Повторение Дня 20
-- ============================================================

-- 1. Все товары
SELECT * FROM products;

-- 2. Только название, категория и цена
SELECT name, category, price FROM products;

-- 3. Товары дороже 100
SELECT name, category, price
FROM products
WHERE price > 100;

-- 4. 5 самых дорогих товаров
SELECT name, category, price
FROM products
ORDER BY price DESC
LIMIT 5;

-- 5. Товары из категории "Электроника" дешевле 500
SELECT name, price
FROM products
WHERE category = 'Электроника' AND price < 500;

-- Всё работает — идём дальше.