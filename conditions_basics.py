a = 10
b = 5

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

temperature = 30

if temperature > 25:
    print("Жарко")

if temperature <= 25:
    print("Не жарко")

    age = 20
has_ticket = True

if age >= 18 and has_ticket:
    print("Можно войти")

age = 16
has_ticket = True

if age >= 18 and has_ticket:
    print("Можно войти")
else:
    print("Нельзя войти")