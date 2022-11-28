#1. Организовать кодовую базу (создать git-репозиторий)
#2. Установить интепретатор Python >=3.8 (https://www.python.org/downloads/)
#3. Изучить установку внешних пакетов через pip (https://pypi.org/)
#4. Установить Jupyter Notebooks (https://jupyter.org/) — если используете VS Code с Питон-сервером Pylance (входит в состав официального Python расширения), то Jupyter будет встроен в интерактивную среду
#5. Изучить основные типы и структуры данных Питона (списки, словари, кортежи, множества)
#6. Описать предметную область на свой выбор при помощи встроенных типов и структур данных

#Строки
city = "Cheyenne"
state = "Wyoming"
location = "West"

print('City:', city, 'State:', state, 'Location:', location)

#bool
boolA = True
boolB = False
if (boolA): print("True")
if (not boolB): print('False')

#Списки
list1 = ["Brown","Apple","Slow","Helmet","Handicap"]
list1.append("Yellow")
print("Not sort:", list1,"Sort:", sorted(list1))

#Словари
states = {'Cities': 'Washingtion '' Detroit'' New York', 'States': 'Texas' 'California' 'Alabama'}
print(states['Cities'], states['States'])

#Кортежи
k = tuple()
k = ('Input', 'Program', 'Window', 'Mouse')
print(k)

#Множества
m1 = {'Flash', 'Enable', 'Monkey', 2022, 1999}
m2 = {'Monkey', 'Elephant', 'Ilya', 'West', 'Wyoming', 1999}
print('Пересечение: ', m1 & m2)
print('Объединение: ', m1 | m2)
print('Разность: ', m1 - m2)
print('Симметрическая разность: ', m1 ^ m2)



