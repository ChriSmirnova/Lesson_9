course = {'title': 'AQA', 'language': 'Python', 'level': 'PRO', 'frame': 'pytest'}

try:
    key = input("Введіть ключ для отримання значення: ")
    value = course[key]
    print(f"Значення для ключа '{key}': {value}")
except KeyError:
    print("Помилка: такого ключа не існує в словнику.")