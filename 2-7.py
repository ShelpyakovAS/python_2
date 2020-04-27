"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def lots_of(n, answer=0):
    answer += n
    if n > 0:
        return lots_of(n - 1, answer)
    else:
        return answer


n = int(input('Введите любое натуральное число: '))
if lots_of(n) == n * (n + 1) / 2:
    print('Равенство выполняется!')
else:
    print('Равенство не выполняется!')
