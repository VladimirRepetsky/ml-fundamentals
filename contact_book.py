contacts = {}

while True:
    print("\n--- Телефонная книга ---")
    print("1. Добавить контакт")
    print("2. Найти контакт")
    print("3. Показать все контакты")
    print("4. Удалить контакт")
    print("5. Выйти")

    choice = input("Выберите действие: ")

    if choice == "1":
        name = input("Имя: ")
        phone = input("Телефон: ")
        contacts[name] = phone
        print("Контакт добавлен.")

    elif choice == "2":
        name = input("Кого найти? ")
        if name in contacts:
            print(f"{name}: {contacts[name]}")
        else:
            print("Контакт не найден.")

    elif choice == "3":
        if len(contacts) == 0:
            print("Книга пуста.")
        else:
            for name, phone in contacts.items():
                print(f"{name}: {phone}")

    elif choice == "4":
        name = input("Кого удалить? ")
        if name in contacts:
            contacts.pop(name)
            print("Контакт удалён.")
        else:
            print("Контакт не найден.")

    elif choice == "5":
        print("До свидания!")
        break

    else:
        print("Неверный выбор.")