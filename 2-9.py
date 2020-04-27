"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

Пример:
Введите количество чисел: 2
Введите число: 23
Введите число: 2
Наибольшее число по сумме цифр: 23, сумма его цифр: 5

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def use_number(number_2, sum_n=0):
    if number_2 > 0:
        return use_number(number_2 // 10, sum_n + number_2 % 10)
    else:
        return sum_n

def take_number(number, max_n=0):
    if number > 0:
        number_2 = int(input('Введите число: '))
        if use_number(max_n) < use_number(number_2):
            return take_number(number-1, max_n=number_2)
        else:
            return take_number(number-1, max_n)
    else:
        print(f'Наибольшее число по сумме цифр: {max_n}, сумма его цифр: {use_number(max_n)}')

number = int(input('Введите количество чисел: '))
take_number(number)