fruits = ["apple", "banana", "cherry", "mango"]

for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")

    names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

print("\nРезультаты студентов:")

for name, score in zip(names, scores):
    print(f"{name}: {score}")

    subjects = ["python", "fastapi", "docker"]
levels = ["junior", "middle", "senior"]

skills = dict(zip(subjects, levels))

print("\nСловарь навыков:")
print(skills)

