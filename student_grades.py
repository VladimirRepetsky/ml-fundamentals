grades = {
    "math": 90,
    "python": 85,
    "ml_basics": 88,
    "english": 79
}

print("Оценки студента:")
for subject, grade in grades.items():
    print(f"{subject}: {grade}")

average = sum(grades.values()) / len(grades)

print(f"Средний балл: {average:.2f}")

best_subject = max(grades, key=grades.get)
worst_subject = min(grades, key=grades.get)

print("Лучший предмет:", best_subject)
print("Худший предмет:", worst_subject)