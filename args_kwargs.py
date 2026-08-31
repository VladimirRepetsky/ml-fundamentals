def sum_all(*args):
    total = 0

    for number in args:
        total += number

    return total


print(sum_all(1, 2))
print(sum_all(1, 2, 3))
print(sum_all(1, 2, 3, 4, 5))

def show_scores(subject, *scores):
    print("Предмет:", subject)
    print("Оценки:", scores)

    average = sum(scores) / len(scores)
    print("Средний балл:", round(average, 2))
    print("-" * 30)


show_scores("Math", 5, 4, 5, 3)
show_scores("Python", 5, 5, 4, 5, 5)

def build_profile(**kwargs):
    print("Профиль пользователя:")

    for key, value in kwargs.items():
        print(f"{key}: {value}")

    print("-" * 30)


build_profile(name="Vladimir", age=25, city="Moscow")
build_profile(name="Alice", profession="Data Scientist", level="Middle")

def create_report(title, *items, **metadata):
    print("Отчёт:", title)
    print("Элементы:", items)
    print("Метаданные:", metadata)
    print("-" * 30)


create_report(
    "ML Progress",
    "Python",
    "Pandas",
    "FastAPI",
    author="Vladimir",
    day=8,
    status="in progress"
)

def create_config(model_name, **parameters):
    config = {
        "model_name": model_name
    }

    config.update(parameters)

    return config


my_config = create_config(
    "distilbert-base-uncased-finetuned-sst-2-english",
    batch_size=16,
    temperature=0.7,
    max_length=128
)

print(my_config)