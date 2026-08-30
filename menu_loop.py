while True:
    print("\n--- Меню ---")
    print("1. Показать приветствие")
    print("2. Показать сообщение")
    print("3. Выйти")

    choice = input("Выберите действие: ")

    if choice == "1":
        print("Привет!")
    elif choice == "2":
        print("Сегодня отличный день для обучения.")
    elif choice == "3":
        print("Выход из программы.")
        break
    else:
        print("Неверный выбор. Попробуйте снова.")