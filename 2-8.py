"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.

Пример:
Сколько будет чисел? - 2
Какую цифру считать? - 3
Число 1: 223
Число 2: 21
Было введено 1 цифр '3'

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def use_number(m, s, count=0):
    if m > 0:
        if m % 10 == s:
            return use_number(m // 10, s,count+1)
        else:
            return use_number(m // 10, s, count)
    else:
        return (count)


def take_number(n, s, count=0):
    if n > 0:
        m = int(input('Введите число: '))
        return take_number(n-1, s, count+use_number(m, s))
    else:
        print(f'Было введено {count} цифр {s}')
        return
n = int(input('Сколько будет чисел? '))
s = int(input('Какую цифру считать? '))

take_number(n, s)




