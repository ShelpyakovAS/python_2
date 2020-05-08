"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
from memory_profiler import profile
from memory_profiler import memory_usage
from time import process_time
from random import random


@profile
def eratosthenes(i):
    n = [2]
    number = 2
    while i != (n.index(max(n)))+1:
        is_simple = True
        for j in n:
            if number % j == 0:
                number += 1
                is_simple = False
        if is_simple:
            n.append(number)
            number += 1
    return max(n)



eratosthenes(100)



@profile
def qwe1(i):
    n = i
    a = [0] * n
    for i in range(n):
        a[i] = int(random() * 100)

    min_id = a.index(min(a))
    max_id = a.index(max(a))

    if min_id > max_id:
        min_id, max_id = max_id, min_id

    summa = 0
    for i in range(min_id + 1, max_id):
        summa += a[i]
    print(f'Сумма элементов между минимальным ({min(a)})  и максимальным ({max(a)}) элементами: {summa}')


qwe1(50000)


@profile
def qwe2():
    say_num = int(input('Введите количество предприятий для расчета прибыли: '))
    sum_year_all = 0
    min_sum = ''
    max_sum = ''
    for i in range(1, say_num + 1):
        say_name = input('Введите название предприятия: ')
        say_money = input('через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ')
        sum_year = say_money.split(' ')
        sum_year = int(sum_year[0]) + int(sum_year[1]) + int(sum_year[2]) + int(sum_year[3])
        globals()['company' + str(i)] = (say_name, say_money, sum_year)
        sum_year_all += sum_year

    for i in range(1, say_num + 1):
        if sum_year_all / say_num > globals()['company' + str(i)][2]:
            min_sum = min_sum + ', ' + (globals()['company' + str(i)][0])
        else:
            max_sum = max_sum + ', ' + (globals()['company' + str(i)][0])

    print(f'Средняя годовая прибыль всех предприятий: {sum_year_all / say_num}')
    print(f'Предприятия, с прибылью выше среднего значения: {max_sum}')
    print(f'Предприятия, с прибылью ниже среднего значения: {min_sum}')

qwe2()
'''
Line #    Mem usage    Increment   Line Contents
================================================
    20     13.6 MiB     13.6 MiB   @profile
    21                             def eratosthenes(i):
    22     13.6 MiB      0.0 MiB       n = [2]
    23     13.6 MiB      0.0 MiB       number = 2
    24     13.6 MiB      0.0 MiB       while i != (n.index(max(n)))+1:
    25     13.6 MiB      0.0 MiB           is_simple = True
    26     13.6 MiB      0.0 MiB           for j in n:
    27     13.6 MiB      0.0 MiB               if number % j == 0:
    28     13.6 MiB      0.0 MiB                   number += 1
    29     13.6 MiB      0.0 MiB                   is_simple = False
    30     13.6 MiB      0.0 MiB           if is_simple:
    31     13.6 MiB      0.0 MiB               n.append(number)
    32     13.6 MiB      0.0 MiB               number += 1
    33     13.6 MiB      0.0 MiB       return max(n)


Сумма элементов между минимальным (0)  и максимальным (99) элементами: 1324
Filename: C:/Users/ShelpyakovAS/Desktop/python/python_study_2/6-1.py

Line #    Mem usage    Increment   Line Contents
================================================
    41     13.6 MiB     13.6 MiB   @profile
    42                             def qwe1(i):
    43     13.6 MiB      0.0 MiB       n = i
    44     13.8 MiB      0.2 MiB       a = [0] * n
    45     13.8 MiB      0.0 MiB       for i in range(n):
    46     13.8 MiB      0.0 MiB           a[i] = int(random() * 100)
    47                             
    48     13.8 MiB      0.0 MiB       min_id = a.index(min(a))
    49     13.8 MiB      0.0 MiB       max_id = a.index(max(a))
    50                             
    51     13.8 MiB      0.0 MiB       if min_id > max_id:
    52     13.8 MiB      0.0 MiB           min_id, max_id = max_id, min_id
    53                             
    54     13.8 MiB      0.0 MiB       summa = 0
    55     13.8 MiB      0.0 MiB       for i in range(min_id + 1, max_id):
    56     13.8 MiB      0.0 MiB           summa += a[i]
    57     13.8 MiB      0.0 MiB       print(f'Сумма элементов между минимальным ({min(a)})  и максимальным ({max(a)}) элементами: {summa}')


Введите количество предприятий для расчета прибыли: 4
Введите название предприятия: qwe1
через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): 159 1566 4569 1235
Введите название предприятия: qwe2
через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): 4598 4568 656 4569
Введите название предприятия: qwe3
через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): 1236 6548 9875 6548
Введите название предприятия: qwe4
через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): 1236 654 654 654
Средняя годовая прибыль всех предприятий: 12331.25
Предприятия, с прибылью выше среднего значения: , qwe2, qwe3
Предприятия, с прибылью ниже среднего значения: , qwe1, qwe4
Filename: C:/Users/ShelpyakovAS/Desktop/python/python_study_2/6-1.py

Line #    Mem usage    Increment   Line Contents
================================================
    63     13.8 MiB     13.8 MiB   @profile
    64                             def qwe2():
    65     13.8 MiB      0.0 MiB       say_num = int(input('Введите количество предприятий для расчета прибыли: '))
    66     13.8 MiB      0.0 MiB       sum_year_all = 0
    67     13.8 MiB      0.0 MiB       min_sum = ''
    68     13.8 MiB      0.0 MiB       max_sum = ''
    69     13.9 MiB      0.0 MiB       for i in range(1, say_num + 1):
    70     13.9 MiB      0.0 MiB           say_name = input('Введите название предприятия: ')
    71     13.9 MiB      0.1 MiB           say_money = input('через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ')
    72     13.9 MiB      0.0 MiB           sum_year = say_money.split(' ')
    73     13.9 MiB      0.0 MiB           sum_year = int(sum_year[0]) + int(sum_year[1]) + int(sum_year[2]) + int(sum_year[3])
    74     13.9 MiB      0.0 MiB           globals()['company' + str(i)] = (say_name, say_money, sum_year)
    75     13.9 MiB      0.0 MiB           sum_year_all += sum_year
    76                             
    77     13.9 MiB      0.0 MiB       for i in range(1, say_num + 1):
    78     13.9 MiB      0.0 MiB           if sum_year_all / say_num > globals()['company' + str(i)][2]:
    79     13.9 MiB      0.0 MiB               min_sum = min_sum + ', ' + (globals()['company' + str(i)][0])
    80                                     else:
    81     13.9 MiB      0.0 MiB               max_sum = max_sum + ', ' + (globals()['company' + str(i)][0])
    82                             
    83     13.9 MiB      0.0 MiB       print(f'Средняя годовая прибыль всех предприятий: {sum_year_all / say_num}')
    84     13.9 MiB      0.0 MiB       print(f'Предприятия, с прибылью выше среднего значения: {max_sum}')
    85     13.9 MiB      0.0 MiB       print(f'Предприятия, с прибылью ниже среднего значения: {min_sum}')
    
Исходя из всех трех таблиц видно что пробленых мест в плане выделения памяти в них нет.
В целом я много чего проверил из предыдущих заданий и графики везде такие. В большинстве случаев наш объем данных для
обработки ниже 0,1. Не стал вставлять сюда рекурсии - много повторений нулевых таблиц. Пробывал memory_usage с
process_time как вы показывали. Хорошо видно объем и время даже если оно мизерное. Плохо что не понятно на что выделятся
ну или делать отсечки внутри функции. (Изначально сделал засечки на функции не убрав @profile ахудивился немного)
Версия Python 3.8.0 Разрядность ОС X64
'''


