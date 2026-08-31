def apply_discount(price, discount=10):
    final_price = price * (1 - discount / 100)
    return final_price


def create_profile(name, age, city="Unknown", **extra):
    profile = {
        "name": name,
        "age": age,
        "city": city
    }

    profile.update(extra)

    return profile


def average(*numbers):
    if len(numbers) == 0:
        return 0

    return sum(numbers) / len(numbers)


def build_ml_config(model_name, **parameters):
    config = {
        "model_name": model_name
    }

    config.update(parameters)

    return config


print("Цена без скидки:", 1000)
print("Цена со скидкой 10%:", apply_discount(1000))
print("Цена со скидкой 25%:", apply_discount(1000, 25))

print()

profile1 = create_profile("Vladimir", 25)
profile2 = create_profile("Alice", 30, "Berlin", profession="Data Scientist", level="Middle")

print(profile1)
print(profile2)

print()

print("Среднее:", average())
print("Среднее:", average(5))
print("Среднее:", average(5, 10, 15))
print("Среднее:", average(1, 2, 3, 4, 5))

print()

config = build_ml_config(
    "distilbert-base-uncased-finetuned-sst-2-english",
    batch_size=16,
    temperature=0.7,
    max_length=128
)

print(config)