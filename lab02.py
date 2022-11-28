# 1 Организация кодовой базы в соответсвии с требованиям PEP8 и область видимость переменных
# 2 Библиотека ГСЧ

# Объявляем библиотеки(массивы и ГСЧ)
from array import array
import random

# Объявляем глобальные переменные
x = 5
y = 15
str = 'Python'
my_array_int = array('i',[1,2,3,4,5])
my_array_str = array('u',['a','b','c','d','f'])

def function():
    # Получаем глобальную переменную внутри функции
    print(x)
    # Для изменения глобальной переменной внутри функции необходимо использовать ключевое слово global
    global y
    y = 10
    print(y)
    # При использовании переменной в функции с похожим названием что и у глобальной, переменная станет локальной в данной функции
    my_array_int = array('i',[5,4,3,2,1])
    for i in range(len(my_array_int)):
        # Изменение элементов массива с помощью ГСЧ
        my_array_int[i] = random.randint(1, 100)
        print(my_array_int[i])
    # Выбор элемента из глобальной строки str c помощью метода choice
    char = random.choice(str)
    print(char)

def main():
    function()

if __name__ == "__main__":
	main()