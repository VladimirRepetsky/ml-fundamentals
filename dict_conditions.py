student = {
    "name": "Vladimir",
    "python": 85,
    "ml_basics": 90,
    "english": 72
}

print(f"Студент: {student['name']}")

for subject, score in student.items():
    if subject == "name":
        continue

    if score >= 85:
        status = "отлично"
    elif score >= 70:
        status = "хорошо"
    else:
        status = "нужно подтянуть"

    print(f"{subject}: {score} ({status})")