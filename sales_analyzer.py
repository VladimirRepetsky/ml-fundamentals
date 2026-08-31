from functools import reduce

sales = [
    {"product": "apple", "price": 120, "quantity": 3},
    {"product": "bread", "price": 80, "quantity": 2},
    {"product": "milk", "price": 150, "quantity": 1},
    {"product": "cheese", "price": 450, "quantity": 2},
    {"product": "coffee", "price": 600, "quantity": 1}
]


def calculate_revenue(sale):
    return sale["price"] * sale["quantity"]


# 1. Доход по каждому товару
revenues = list(map(calculate_revenue, sales))

print("Доход по каждому товару:")

for sale, revenue in zip(sales, revenues):
    print(f"{sale['product']}: {revenue}")


# 2. Общий доход
total_revenue = reduce(lambda acc, revenue: acc + revenue, revenues, 0)

print("\nОбщий доход:", total_revenue)


# 3. Товары с доходом 300 и выше
high_revenue_sales = list(
    filter(lambda sale: calculate_revenue(sale) >= 300, sales)
)

print("\nТовары с доходом 300 и выше:")

for sale in high_revenue_sales:
    revenue = calculate_revenue(sale)
    print(f"{sale['product']}: {revenue}")


# 4. Сортировка товаров по доходу
sorted_sales = sorted(
    sales,
    key=lambda sale: calculate_revenue(sale),
    reverse=True
)

print("\nТовары по доходу, от большего к меньшему:")

for sale in sorted_sales:
    revenue = calculate_revenue(sale)
    print(f"{sale['product']}: {revenue}")

top_sale = max(sales, key=lambda sale: calculate_revenue(sale))

print("\nЛучший товар по доходу:")
print(f"{top_sale['product']}: {calculate_revenue(top_sale)}")