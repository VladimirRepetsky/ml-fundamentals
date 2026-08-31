filename = "diary.txt"

print("--- Мини-дневник ---")

while True:
    print("\n1. Добавить запись")
    print("2. Показать записи")
    print("3. Выйти")

    choice = input("Выберите действие: ")

    if choice == "1":
        note = input("Введите запись: ")

        try:
            with open(filename, "a", encoding="utf-8") as file:
                file.write(note + "\n")
            print("Запись сохранена.")
        except OSError:
            print("Ошибка при записи файла.")

    elif choice == "2":
        try:
            with open(filename, "r", encoding="utf-8") as file:
                lines = file.readlines()

            if len(lines) == 0:
                print("Дневник пуст.")
            else:
                print("Ваши записи:")
                for index, line in enumerate(lines, start=1):
                    print(f"{index}. {line.strip()}")

        except FileNotFoundError:
            print("Дневник пока не создан.")

    elif choice == "3":
        print("До свидания!")
        break

    else:
        print("Неверный выбор.")

