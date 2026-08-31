def factorial(n):
    if n < 0:
        return None

    result = 1

    for number in range(2, n + 1):
        result *= number

    return result


def is_palindrome(text):
    punctuation = ".,!?;:()\"'- "

    clean_text = ""

    for char in text.lower():
        if char not in punctuation:
            clean_text += char

    return clean_text == clean_text[::-1]


def sum_list(numbers):
    total = 0

    for number in numbers:
        total += number

    return total


print("Факториал 0:", factorial(0))
print("Факториал 1:", factorial(1))
print("Факториал 5:", factorial(5))
print("Факториал 7:", factorial(7))

print()

print("Палиндром 'шалаш':", is_palindrome("шалаш"))
print("Палиндром 'hello':", is_palindrome("hello"))
print("Палиндром 'А роза упала на лапу Азора':", is_palindrome("А роза упала на лапу Азора"))

print()

print("Сумма списка:", sum_list([10, 20, 30, 40]))
print("Сумма списка:", sum_list([1, 2, 3, 4, 5]))


def is_palindrome_verbose(text):
    punctuation = ".,!?;:()\"'- "

    clean_text = ""

    for char in text.lower():
        if char not in punctuation:
            clean_text += char

    reversed_text = clean_text[::-1]

    print("Оригинал:", text)
    print("Очищенный текст:", clean_text)
    print("Перевёрнутый текст:", reversed_text)
    print("Это палиндром:", clean_text == reversed_text)
    print("-" * 40)


is_palindrome_verbose("шалаш")
is_palindrome_verbose("hello")
is_palindrome_verbose("А роза упала на лапу Азора")

def factorial_recursive(n):
    if n < 0:
        return None

    if n <= 1:
        return 1

    return n * factorial_recursive(n - 1)


print("Рекурсивный факториал 5:", factorial_recursive(5))
print("Рекурсивный факториал 7:", factorial_recursive(7))