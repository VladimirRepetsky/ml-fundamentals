import pandas as pd

orders = pd.read_csv("data/orders.csv")
customers = pd.read_csv("data/customers.csv")

print("=== Orders ===")
print(orders)
print("\n=== Customers ===")
print(customers)

# ============================================================
# 1. INNER JOIN (по умолчанию)
# ============================================================

print("\n=== INNER JOIN ===")
inner = pd.merge(orders, customers, on="customer_id")
print(inner)
print(f"Строк: {len(inner)} (только совпадающие customer_id)")

# ============================================================
# 2. LEFT JOIN
# ============================================================

print("\n=== LEFT JOIN ===")
left = pd.merge(orders, customers, on="customer_id", how="left")
print(left)
print(f"Строк: {len(left)} (все заказы, даже без клиента)")

# ============================================================
# 3. RIGHT JOIN
# ============================================================

print("\n=== RIGHT JOIN ===")
right = pd.merge(orders, customers, on="customer_id", how="right")
print(right)
print(f"Строк: {len(right)} (все клиенты, даже без заказов)")

# ============================================================
# 4. OUTER JOIN
# ============================================================

print("\n=== OUTER JOIN ===")
outer = pd.merge(orders, customers, on="customer_id", how="outer")
print(outer)
print(f"Строк: {len(outer)} (все записи из обеих таблиц)")

# ============================================================
# 5. CONCAT: вертикальное объединение
# ============================================================

print("\n=== CONCAT (вертикальное) ===")
df1 = pd.DataFrame({"name": ["Alice", "Bob"], "score": [85, 92]})
df2 = pd.DataFrame({"name": ["Charlie", "David"], "score": [78, 88]})

combined = pd.concat([df1, df2], ignore_index=True)
print(combined)

# ============================================================
# 6. CONCAT: горизонтальное объединение
# ============================================================

print("\n=== CONCAT (горизонтальное) ===")
names = pd.DataFrame({"name": ["Alice", "Bob", "Charlie"]})
scores = pd.DataFrame({"score": [85, 92, 78]})

side_by_side = pd.concat([names, scores], axis=1)
print(side_by_side)

# ============================================================
# 7. ПРАКТИЧЕСКИЙ ПРИМЕР: анализ заказов
# ============================================================

print("\n=== Практический пример ===")

merged = pd.merge(orders, customers, on="customer_id", how="left")

print("Общая сумма по клиентам:")
print(merged.groupby("name")["amount"].sum().sort_values(ascending=False))

print("\nСредний чек по городам:")
print(merged.groupby("city")["amount"].mean().round(2))

print("\nКоличество заказов по продуктам:")
print(merged.groupby("product").size().sort_values(ascending=False))