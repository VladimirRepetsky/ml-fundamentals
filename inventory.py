inventory = {
    "apple": 5,
    "banana": 2,
    "orange": 8
}

print("Инвентарь:")
for item, quantity in inventory.items():
    print(f"{item}: {quantity}")

total_items = sum(inventory.values())
print("Всего фруктов:", total_items)

most_available_item = max(inventory, key=inventory.get)
least_available_item = min(inventory, key=inventory.get)

print("Больше всего:", most_available_item)
print("Меньше всего:", least_available_item)