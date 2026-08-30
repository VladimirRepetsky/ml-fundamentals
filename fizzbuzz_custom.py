start = int(input("Введите начальное число: "))
end = int(input("Введите конечное число: "))

for number in range(start, end + 1):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)