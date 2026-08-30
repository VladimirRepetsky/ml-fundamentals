import random

secret_number = random.randint(1, 100)
attempts = 0

print("Я загадал число от 1 до 100.")
print("Попробуй его угадать.")

while True:
    user_input = input("Введи число: ")

    if not user_input.isdigit():
        print("Пожалуйста, введи целое число от 1 до 100.")
        continue

    guess = int(user_input)
    attempts += 1

    if guess < secret_number:
        print("Слишком мало. Попробуй ещё раз.")
    elif guess > secret_number:
        print("Слишком много. Попробуй ещё раз.")
    else:
        print(f"Победа! Ты угадал число {secret_number} за {attempts} попыток.")
        break