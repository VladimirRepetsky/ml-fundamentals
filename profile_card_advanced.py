name = input("Введите имя: ")
profession = input("Введите профессию или цель: ")
city = input("Введите город: ")
age = int(input("Введите возраст: "))
months = int(input("Сколько месяцев вы планируете учиться: "))

days = months * 30
hours = months * 30 * 2

line = "=" * 45

summary = f"""
{line}
ML Learning Card
{line}
Name: {name}
Target: {profession}
City: {city}
Age: {age}
Duration: {months} months
Approximate days: {days}
Approximate hours: {hours}
Status: In progress
{line}
"""

print(summary)