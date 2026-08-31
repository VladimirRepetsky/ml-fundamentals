def sum_list(numbers):
    total = 0

    for number in numbers:
        total += number

    return total


data = [10, 20, 30, 40, 50]

print("Сумма элементов:", sum_list(data))

def is_palindrome(text):
    clean_text = text.lower().replace(" ", "")
    reversed_text = clean_text[::-1]

    return clean_text == reversed_text


print(is_palindrome("шалаш"))
print(is_palindrome("hello"))
print(is_palindrome("А роза упала на лапу Азора"))

def factorial(n):
    if n < 0:
        return None

    result = 1

    for number in range(2, n + 1):
        result *= number

    return result


print(factorial(0))
print(factorial(1))
print(factorial(3))
print(factorial(5))
print(factorial(7))

def count_words(words):
    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency


text = "python is good and python is useful"

words = text.split()

result = count_words(words)

print(result)