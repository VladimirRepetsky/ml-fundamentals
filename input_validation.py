while True:
    age = input("Введите ваш возраст: ")

    if age.isdigit():
        age = int(age)
        break
    else:
        print("Пожалуйста, введите число.")

print(f"Ваш возраст: {age}")