shopping_list = []

while True:
    print("\n--- Список покупок ---")
    print("1. Добавить товар")
    print("2. Удалить товар")
    print("3. Показать список")
    print("4. Выйти")

    choice = input("Выберите действие (1-4): ")

    if choice == "1":
        item = input("Что добавить? ")
        shopping_list.append(item)
        print(f"'{item}' добавлен в список.")

    elif choice == "2":
        item = input("Что удалить? ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'{item}' удалён из списка.")
        else:
            print(f"'{item}' не найден в списке.")

    elif choice == "3":
        if len(shopping_list) == 0:
            print("Список пуст.")
        else:
            print("Ваш список:")
            for i, item in enumerate(shopping_list):
                print(f"{i + 1}. {item}")

    elif choice == "4":
        print("До свидания!")
        break

    else:
        print("Неверный выбор. Попробуйте снова.")