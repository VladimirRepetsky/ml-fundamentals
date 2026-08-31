def add(a: int, b: int) -> int:
    return a + b


def greet(name: str) -> str:
    return f"Hello, {name}"


def is_even(number: int) -> bool:
    return number % 2 == 0


print(add(2, 3))
print(greet("Vladimir"))
print(is_even(10))