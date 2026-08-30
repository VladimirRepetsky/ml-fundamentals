import random

secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 7

print("Я загадал число от 1 до 100.")
print(f"У тебя есть {max_attempts} попыток.")

while attempts < max_attempts:
    user_input = input("Введи число: ")

    if not user_input.isdigit():
        print("Пожалуйста, введи целое число от 1 до 100.")
        continue

    guess = int(user_input)
    attempts += 1

    remaining_attempts = max_attempts - attempts

    if guess < secret_number:
        print(f"Слишком мало. Осталось попыток: {remaining_attempts}")
    elif guess > secret_number:
        print(f"Слишком много. Осталось попыток: {remaining_attempts}")
    else:
        print(f"Победа! Ты угадал число {secret_number} за {attempts} попыток.")
        break

if attempts == max_attempts and guess != secret_number:
    print(f"Попытки закончились. Загаданное число было: {secret_number}")