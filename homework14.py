# Напишите функцию для парсинга номерных знаков автомоблей Украины (стандарты - AА1234BB, 12 123-45AB, a12345BC)
# с помощью регулярных выражений. Функция принимает строку и возвращает None если строка не является номерным знаком.
# Если является номерным знаком - возвращает саму строку.

import re


num = "AА123s4BB"

def numberplate(num):
    var1 = '[A-ZА-Я]{2}\d{4}[A-ZА-Я]{2}'
    var2 = '\d{2}\s\d{3}-\d{2}[A-ZА-Я]{2}'
    var3 = '[а-яa-zA-ZА-Я]\d{5}[A-ZА-Я]{2}'

    if re.findall(var1, num):
        return print(num)
    elif re.findall(var2, num):
        return print(num)
    elif re.findall(var3, num):
        return print(num)
    else:
        return None


numberplate(num)
