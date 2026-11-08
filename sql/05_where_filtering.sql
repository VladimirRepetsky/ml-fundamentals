-- ============================================================
-- День 20: Фильтрация через WHERE
-- ============================================================

-- 1. Равенство
SELECT name, category, price
FROM products
WHERE category = 'Электроника';

-- 2. Больше / меньше
SELECT name, price
FROM products
WHERE price > 100;

SELECT name, price
FROM products
WHERE price >= 500;

SELECT name, price
FROM products
WHERE price < 50;

SELECT name, price
FROM products
WHERE price <= 25;

-- 3. Не равно
SELECT name, category
FROM products
WHERE category != 'Одежда';

-- Альтернативный синтаксис
SELECT name, category
FROM products
WHERE category <> 'Одежда';

-- 4. Диапазон значений (BETWEEN)
SELECT name, price
FROM products
WHERE price BETWEEN 50 AND 200;

-- То же самое через >= и <=
SELECT name, price
FROM products
WHERE price >= 50 AND price <= 200;

-- 5. Список значений (IN)
SELECT name, category
FROM products
WHERE category IN ('Электроника', 'Книги');

-- То же самое через OR
SELECT name, category
FROM products
WHERE category = 'Электроника' OR category = 'Книги';

-- 6. Исключение из списка (NOT IN)
SELECT name, category
FROM products
WHERE category NOT IN ('Продукты', 'Дом и сад');

-- 7. Поиск по шаблону (LIKE)
-- % означает "любое количество любых символов"
-- _ означает "один любой символ"

-- Товары, название которых начинается с "Ноутбук"
SELECT name, price
FROM products
WHERE name LIKE 'Ноутбук%';

-- Товары, в названии которых есть "кофе" (без учёта регистра через ILIKE)
SELECT name, price
FROM products
WHERE name ILIKE '%кофе%';

-- Товары, название которых заканчивается на "ый"
SELECT name, price
FROM products
WHERE name LIKE '%ый';

-- 8. Проверка на пустоту (IS NULL / IS NOT NULL)
-- В нашей таблице нет пустых значений, но это важный синтаксис
SELECT name, price
FROM products
WHERE price IS NOT NULL;

-- 9. Комбинированные условия (AND, OR, NOT)
SELECT name, category, price
FROM products
WHERE category = 'Электроника' AND price > 500;

SELECT name, category, price
FROM products
WHERE category = 'Книги' OR price < 10;

SELECT name, category, price
FROM products
WHERE NOT category = 'Продукты';

-- 10. Сложные комбинированные условия
SELECT name, category, price, quantity
FROM products
WHERE
    (category = 'Электроника' AND price > 1000)
    OR
    (category = 'Одежда' AND quantity > 50);

-- 11. Фильтрация с вычислением
SELECT name, price, quantity, price * quantity AS total_value
FROM products
WHERE price * quantity > 5000
ORDER BY total_value DESC;