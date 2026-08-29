name = input("Введите имя: ")
profession = input("Введите профессию или цель: ")
city = input("Введите город: ")
age = int(input("Введите возраст: "))
years_in_ml = int(input("Сколько месяцев вы планируете учиться: "))

line = "-" * 40

profile = f"""
{line}
Profile Card
{line}
Name: {name}
Goal: {profession}
City: {city}
Age: {age}
Learning plan: {years_in_ml} months
{line}
"""

print(profile)