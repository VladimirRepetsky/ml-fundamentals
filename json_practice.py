import json

user = {
    "name": "Vladimir",
    "age": 25,
    "city": "Moscow",
    "is_learning_ml": True,
    "skills": ["Python", "Git", "GitHub"],
    "progress": {
        "day": 10,
        "topic": "exceptions and files",
        "completed": True
    }
}

with open("user.json", "w", encoding="utf-8") as file:
    json.dump(user, file, ensure_ascii=False, indent=2)

print("Данные сохранены в user.json")

with open("user.json", "r", encoding="utf-8") as file:
    loaded_user = json.load(file)

print("\nДанные из JSON:")
print(loaded_user)

print("\nИмя:", loaded_user["name"])
print("Возраст:", loaded_user["age"])
print("Навыки:", loaded_user["skills"])
print("День обучения:", loaded_user["progress"]["day"])


config = {
    "model_name": "distilbert-base-uncased-finetuned-sst-2-english",
    "temperature": 0.7,
    "max_length": 128
}

config_text = json.dumps(config, indent=2)

print("\nJSON как строка:")
print(config_text)

config_back = json.loads(config_text)

print("\nОбратно в Python:")
print(config_back)
print(config_back["model_name"])


broken_json = '{"name": "Vladimir", "age": 25,}'

try:
    data = json.loads(broken_json)
except json.JSONDecodeError:
    print("\nОшибка: JSON повреждён.")