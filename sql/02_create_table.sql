-- ============================================================
-- День 20: Создание таблицы products
-- ============================================================

-- Убедись, что ты подключён к базе данных ml_fundamentals

-- Удаляем таблицу, если она уже существует
DROP TABLE IF EXISTS products;

-- Создаём таблицу
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    price NUMERIC(10, 2) NOT NULL CHECK (price >= 0),
    quantity INTEGER NOT NULL DEFAULT 0 CHECK (quantity >= 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Добавляем комментарий к таблице
COMMENT ON TABLE products IS 'Каталог товаров магазина для обучения SQL';
COMMENT ON COLUMN products.id IS 'Уникальный идентификатор товара';
COMMENT ON COLUMN products.name IS 'Название товара';
COMMENT ON COLUMN products.category IS 'Категория товара';
COMMENT ON COLUMN products.price IS 'Цена товара';
COMMENT ON COLUMN products.quantity IS 'Количество на складе';
COMMENT ON COLUMN products.created_at IS 'Дата создания записи';