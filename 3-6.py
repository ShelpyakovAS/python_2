"""
Задание_6.	В одномерном массиве найти сумму элементов,
находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.

Подсказки:
1) берем первый минимальный и максимальный
2) не забудьте, что сначала может быть минимальный, потом максимальный
а может - наоборот. во всех этих случаях нужна корректная работа

Пример:
Введите количество элементов в массиве: 10
Массив: [88, 58, 50, 77, 49, 6, 42, 67, 14, 79]
Сумма элементов между минимальным (6)  и максимальным (88) элементами: 234
"""
from random import random

n = int(input('Введите количество элементов в массиве: '))
a = [0]*n
for i in range(n):
    a[i] = int(random()*100)
print(a)

min_id = a.index(min(a))
max_id = a.index(max(a))

if min_id > max_id:
    min_id, max_id = max_id, min_id

summa = 0
for i in range(min_id+1, max_id):
    summa += a[i]
print(f'Сумма элементов между минимальным ({min(a)})  и максимальным ({max(a)}) элементами: {summa}')
