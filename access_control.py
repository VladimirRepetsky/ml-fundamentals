age = int(input("Введите возраст: "))
has_id = input("Есть ли у вас удостоверение? (да/нет): ")

has_id = has_id.lower().strip()

if age >= 18 and has_id == "да":
    print("Доступ разрешён")
else:
    print("Доступ запрещён")