for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end="\t")
    print()

    colors = ["red", "green", "blue"]
sizes = ["S", "M", "L"]

print("\nВарианты товаров:")

for color in colors:
    for size in sizes:
        print(f"{color} - {size}")