celsius = float(input("Введите температуру в градусах Цельсия: "))

fahrenheit = celsius * 9 / 5 + 32
kelvin = celsius + 273.15

print(f"{celsius:.2f} градусов Цельсия = {fahrenheit:.2f} градусов Фаренгейта")
print(f"{celsius:.2f} градусов Цельсия = {kelvin:.2f} градусов Кельвина")