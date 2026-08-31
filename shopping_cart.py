products = {
    "apple": 120,
    "bread": 80,
    "milk": 150,
    "cheese": 450,
    "coffee": 600
}

cart = {}

while True:
    print("\n--- Корзина магазина ---")
    print("1. Показать товары")
    print("2. Добавить товар")
    print("3. Удалить товар")
    print("4. Показать корзину")
    print("5. Оформить заказ")
    print("6. Выйти")

    choice = input("Выберите действие: ")

    if choice == "1":
        print("\nДоступные товары:")
        for product, price in products.items():
            print(f"{product}: {price} руб.")

    elif choice == "2":
        product = input("Введите название товара: ").strip().lower()

        if product not in products:
            print("Такого товара нет в магазине.")
            continue

        quantity = input("Введите количество: ")

        if not quantity.isdigit():
            print("Пожалуйста, введите число.")
            continue

        quantity = int(quantity)

        if quantity <= 0:
            print("Количество должно быть больше нуля.")
            continue

        cart[product] = cart.get(product, 0) + quantity

        print(f"Товар '{product}' добавлен в количестве {quantity}.")

    elif choice == "3":
        product = input("Какой товар удалить? ").strip().lower()

        if product in cart:
            cart.pop(product)
            print(f"Товар '{product}' удалён из корзины.")
        else:
            print("Такого товара нет в корзине.")

    elif choice == "4":
        if len(cart) == 0:
            print("Корзина пуста.")
        else:
            print("\nВаша корзина:")

            total_items = 0
            total_price = 0

            for product, quantity in cart.items():
                price = products[product]
                cost = price * quantity

                total_items += quantity
                total_price += cost

                print(f"{product}: {quantity} x {price} = {cost} руб.")

            print("\nВсего товаров:", total_items)
            print("Общая сумма:", total_price, "руб.")

    elif choice == "5":
        if len(cart) == 0:
            print("Корзина пуста. Невозможно оформить заказ.")
            continue

        total_price = 0

        for product, quantity in cart.items():
            total_price += products[product] * quantity

        discount = 0

        if total_price >= 1000:
            discount = total_price * 0.10

        final_price = total_price - discount

        print("\n--- Оформление заказа ---")
        print("Сумма:", total_price, "руб.")

        if discount > 0:
            print("Скидка 10%:", discount, "руб.")

        print("Итого к оплате:", final_price, "руб.")

        cart.clear()

        print("Заказ оформлен. Корзина очищена.")

    elif choice == "6":
        print("До свидания!")
        break

    else:
        print("Неверный выбор. Попробуйте снова.")