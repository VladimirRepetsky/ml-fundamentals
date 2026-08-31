import json

FILENAME = "profiles.json"


def load_profiles(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

            if isinstance(data, list):
                return data
            else:
                print("Файл имеет неверный формат. Создаём новый список.")
                return []

    except FileNotFoundError:
        print("Файл не найден. Создаём новый список.")
        return []

    except json.JSONDecodeError:
        print("Файл повреждён. Создаём новый список.")
        return []


def save_profiles(profiles, filename):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(profiles, file, ensure_ascii=False, indent=2)
        return True
    except OSError:
        print("Ошибка при сохранении файла.")
        return False


def add_profile(profiles):
    name = input("Введите имя: ").strip()

    if name == "":
        print("Имя не может быть пустым. Профиль не добавлен.")
        return

    age_input = input("Введите возраст: ").strip()

    try:
        age = int(age_input)

        if age <= 0:
            raise ValueError

    except ValueError:
        print("Некорректный возраст. Профиль не добавлен.")
        return

    track = input("Введите трек обучения: ").strip()

    profile = {
        "name": name,
        "age": age,
        "track": track
    }

    profiles.append(profile)
    print("Профиль добавлен.")


def show_profiles(profiles):
    if len(profiles) == 0:
        print("Список профилей пуст.")
        return

    print("\nСписок профилей:")

    for index, profile in enumerate(profiles, start=1):
        print(f"{index}. {profile['name']}, возраст: {profile['age']}, трек: {profile['track']}")


def delete_profile(profiles):
    show_profiles(profiles)

    if len(profiles) == 0:
        return

    index_input = input("Введите номер профиля для удаления: ")

    try:
        index = int(index_input)

        if index < 1 or index > len(profiles):
            print("Неверный номер.")
            return

        removed = profiles.pop(index - 1)
        print(f"Профиль '{removed['name']}' удалён.")

    except ValueError:
        print("Нужно ввести номер профиля.")


while True:
    print("\n--- Менеджер профилей ---")
    print("1. Добавить профиль")
    print("2. Показать профили")
    print("3. Удалить профиль")
    print("4. Выйти")

    choice = input("Выберите действие: ")

    profiles = load_profiles(FILENAME)

    if choice == "1":
        add_profile(profiles)
        save_profiles(profiles, FILENAME)

    elif choice == "2":
        show_profiles(profiles)

    elif choice == "3":
        delete_profile(profiles)
        save_profiles(profiles, FILENAME)

    elif choice == "4":
        print("До свидания!")
        break

    else:
        print("Неверный выбор.")

