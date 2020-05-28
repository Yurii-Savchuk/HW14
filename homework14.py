# Напишите функцию для парсинга номерных знаков автомоблей Украины (стандарты - AА1234BB, 12 123-45AB, a12345BC)
# с помощью регулярных выражений. Функция принимает строку и возвращает None если строка не является номерным знаком.
# Если является номерным знаком - возвращает саму строку.

import re

num = "AА1234BB"

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


#  Напишите класс, который выбирает из произвольного текста номерные знаки и возвращает их в виде пронумерованного списка

class Numberplate:
    _text = 'asdasdsadf'

    def __init__(self, text):
        self._text = text

    def numberplate_parser(self, text):
        var1 = re.findall('[A-ZА-Я]{2}\d{4}[A-ZА-Я]{2}', text)
        var2 = re.findall('\d{2}\s\d{3}-\d{2}[A-ZА-Я]{2}', text)
        var3 = re.findall('[а-яa-zA-ZА-Я]\d{5}[A-ZА-Я]{2}', text)
        lst = list()
        n = 0


        if var1:
            n += 1
            my_str = f'{n} -- {var1}'
            lst.append(my_str)
        if var2:
            n += 1
            my_str = f'{n} -- {var2}'
            lst.append(my_str)
        if var3:
            n += 1
            my_str = f'{n} -- {var3}'
            lst.append(my_str)

        return print(lst)


res = Numberplate('asdafafds AА123s4BB aczxcx')
print(res.numberplate_parser('asdafafds AА1234BB aczxcx AА1234BB a12345BC'))
