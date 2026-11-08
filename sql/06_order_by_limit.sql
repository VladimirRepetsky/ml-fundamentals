-- ============================================================
-- День 20: Сортировка и ограничение
-- ============================================================

-- 1. Сортировка по возрастанию (по умолчанию)
SELECT name, price
FROM products
ORDER BY price;

-- 2. Сортировка по убыванию
SELECT name, price
FROM products
ORDER BY price DESC;

-- 3. Сортировка по нескольким столбцам
-- Сначала по категории (по алфавиту), затем по цене (по убыванию)
SELECT name, category, price
FROM products
ORDER BY category ASC, price DESC;

-- 4. Сортировка по алиасу
SELECT name, price, price * quantity AS total_value
FROM products
ORDER BY total_value DESC;

-- 5. Ограничение количества строк (LIMIT)
-- Получить первые 5 товаров
SELECT name, price
FROM products
LIMIT 5;

-- 6. Получить 5 самых дорогих товаров
SELECT name, category, price
FROM products
ORDER BY price DESC
LIMIT 5;

-- 7. Получить 3 самых дешёвых товара
SELECT name, category, price
FROM products
ORDER BY price ASC
LIMIT 3;

-- 8. Получить 3 самых дорогих товара из категории "Электроника"
SELECT name, price
FROM products
WHERE category = 'Электроника'
ORDER BY price DESC
LIMIT 3;

-- 9. Пагинация: LIMIT и OFFSET
-- Пропустить первые 5 строк и взять следующие 5
SELECT name, price
FROM products
ORDER BY price
LIMIT 5 OFFSET 5;

-- 10. Товар с наибольшим количеством на складе
SELECT name, quantity
FROM products
ORDER BY quantity DESC
LIMIT 1;

-- 11. Товар с наименьшим количеством на складе
SELECT name, quantity
FROM products
ORDER BY quantity ASC
LIMIT 1;

-- 12. Порядок выполнения запроса
-- SQL выполняет запрос в таком порядке:
--   1. FROM products        (из какой таблицы)
--   2. WHERE ...            (фильтрация)
--   3. GROUP BY ...         (группировка)
--   4. HAVING ...           (фильтрация групп)
--   5. SELECT ...           (выбор столбцов)
--   6. ORDER BY ...         (сортировка)
--   7. LIMIT ...            (ограничение)
--
-- Это важно понимать, потому что:
-- - В WHERE нельзя использовать алиасы из SELECT
-- - В ORDER BY можно использовать алиасы из SELECT

-- Пример: правильный порядок
SELECT name, price, price * quantity AS total_value
FROM products
WHERE price > 100          -- фильтр до вычислений в SELECT
ORDER BY total_value DESC  -- сортировка после SELECT
LIMIT 5;                   -- ограничение в конце