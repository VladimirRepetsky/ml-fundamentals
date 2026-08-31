def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"


print(add(2, 3))
print(multiply(4, 5))
print(get_grade(95))
print(get_grade(72))