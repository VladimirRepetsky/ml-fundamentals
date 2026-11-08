-- ============================================================
-- День 20: Практические задания из программы
-- ============================================================
-- Эти задания закрывают требования Недели 4 (часть 1):
-- ✓ Получить все товары.
-- ✓ Получить товары с ценой выше 100.
-- ✓ Получить 5 самых дорогих товаров.
-- ✓ Посчитать общее количество товаров по каждой категории.
-- ✓ Найти категории, где средняя цена выше 150.
-- ============================================================

-- Задание 1: Получить все товары
-- Ожидаемый результат: 28 строк
SELECT * FROM products;

-- Задание 2: Получить товары с ценой выше 100
SELECT name, category, price
FROM products
WHERE price > 100;

-- Задание 3: Получить 5 самых дорогих товаров
SELECT name, category, price
FROM products
ORDER BY price DESC
LIMIT 5;

-- Задание 4: Посчитать общее количество товаров по каждой категории
-- Используем COUNT(*) и GROUP BY
SELECT category, COUNT(*) AS product_count
FROM products
GROUP BY category
ORDER BY product_count DESC;

-- Задание 5: Найти категории, где средняя цена выше 150
-- Используем AVG() и HAVING
SELECT category, ROUND(AVG(price), 2) AS avg_price
FROM products
GROUP BY category
HAVING AVG(price) > 150
ORDER BY avg_price DESC;

-- ============================================================
-- Дополнительные задания для закрепления
-- ============================================================

-- Задание 6: Получить названия и цены товаров из категории "Книги"
SELECT name, price
FROM products
WHERE category = 'Книги';

-- Задание 7: Получить товары, название которых содержит "Ноутбук"
SELECT name, price
FROM products
WHERE name LIKE '%Ноутбук%';

-- Задание 8: Получить товары с ценой от 50 до 200
SELECT name, price
FROM products
WHERE price BETWEEN 50 AND 200
ORDER BY price;

-- Задание 9: Получить 3 самых дешёвых товара из категории "Продукты"
SELECT name, price
FROM products
WHERE category = 'Продукты'
ORDER BY price ASC
LIMIT 3;

-- Задание 10: Получить товары с общим запасом (цена × количество) больше 5000
SELECT name, price, quantity, price * quantity AS total_value
FROM products
WHERE price * quantity > 5000
ORDER BY total_value DESC;

-- Задание 11: Получить уникальные категории
SELECT DISTINCT category FROM products;

-- Задание 12: Посчитать общее количество товаров на складе
SELECT SUM(quantity) AS total_stock FROM products;

-- Задание 13: Получить среднюю цену по всем товарам
SELECT ROUND(AVG(price), 2) AS avg_price FROM products;

-- Задание 14: Получить минимальную и максимальную цену
SELECT
    MIN(price) AS min_price,
    MAX(price) AS max_price
FROM products;

-- Задание 15: Получить товары, которых на складе меньше 20 штук
SELECT name, quantity
FROM products
WHERE quantity < 20
ORDER BY quantity;