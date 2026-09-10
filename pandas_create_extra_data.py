import pandas as pd

# Таблица заказов
orders = pd.DataFrame({
    "order_id": [101, 102, 103, 104, 105, 106],
    "customer_id": [1, 2, 1, 3, 2, 4],
    "product": ["laptop", "phone", "tablet", "laptop", "phone", "monitor"],
    "amount": [1200, 800, 400, 1500, 900, 350],
})

# Таблица клиентов
customers = pd.DataFrame({
    "customer_id": [1, 2, 3, 5],
    "name": ["Alice", "Bob", "Charlie", "Eve"],
    "city": ["Moscow", "Berlin", "London", "Paris"],
})

orders.to_csv("data/orders.csv", index=False)
customers.to_csv("data/customers.csv", index=False)

print("Файлы созданы:")
print("\nOrders:")
print(orders)
print("\nCustomers:")
print(customers)