grades = {
    "math": 90,
    "python": 85,
    "ml_basics": 88,
    "english": 72,
    "statistics": 68
}

total = 0

for subject, score in grades.items():
    total += score
    print(f"{subject}: {score}")

average = total / len(grades)

print("\nСредний балл:", round(average, 2))

passed = {}

for subject, score in grades.items():
    if score >= 75:
        passed[subject] = score

print("\nПредметы с баллом 75 и выше:")
print(passed)

status = {}

for subject, score in grades.items():
    if score >= 85:
        status[subject] = "отлично"
    elif score >= 75:
        status[subject] = "хорошо"
    elif score >= 60:
        status[subject] = "удовлетворительно"
    else:
        status[subject] = "нужно подтянуть"

print("\nСтатусы по предметам:")

for subject, result in status.items():
    print(f"{subject}: {result}")

    