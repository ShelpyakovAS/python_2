"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

Подсказка:
1) возьмите 2-3 задачи, реализованные ранее, сделайте замеры на разных входных данных
2) сделайте для каждой из задач оптимизацию (придумайте что можно оптимизировать)
и также выполните замеры на уже оптимизированных алгоритмах
3) опишите результаты - где, что эффективнее и почему.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
import timeit


def asp():
    a = [8, 3, 15, 6, 4, 2]
    b = []
    for i in a:
        if i % 2 == 0:
            b += [a.index(i)]
    return b


def asp2():
    a = [8, 3, 15, 6, 4, 2]
    b = [a.index(i) for i in a if i % 2 == 0]
    return b


def asp3():
    a = [8, 3, 15, 6, 4, 2]
    b = []
    for i in a:
        if i % 2 == 0:
            b.append(a.index(i))
    return b


print(timeit.timeit("asp()", setup="from __main__ import asp", number=1000))
print(asp())
print(timeit.timeit("asp2()", setup="from __main__ import asp2", number=1000))
print(asp2())
print(timeit.timeit("asp3()", setup="from __main__ import asp3", number=1000))
print(asp3())
'''
Результат
0.0015904999999999982
[0, 3, 4, 5]
0.0015085999999999988
[0, 3, 4, 5]
0.0014657999999999997
[0, 3, 4, 5]
Сложность всех трех решений одинаковая.
встроенный в класс list __add__ затратнее метода list.append
что используется при короткой записе я так и не понял. Но он всегда на 2-ром месте по скорости.
'''


def turn_over(number, number2=''):
    if number > 0:
        a = str(number % 10)
        return turn_over(number // 10, number2 + a)
    else:
        return number2


def turn_over2(number, number2=0):
    if number > 0:
        number2 = number2 * 10 + number % 10
        return turn_over2(number // 10, number2)
    else:
        return number2


def turn_over3(n):
    m = 0
    while n > 0:
        m = m * 10 + n % 10
        n = n // 10
    return m


print(timeit.timeit("turn_over(34568)", setup="from __main__ import turn_over", number=1000))
print(turn_over(34568))
print(timeit.timeit("turn_over2(34568)", setup="from __main__ import turn_over2", number=1000))
print(turn_over2(34568))
print(timeit.timeit("turn_over3(34568)", setup="from __main__ import turn_over3", number=1000))
print(turn_over3(34568))
'''
Результат
0.003082999999999999
86543
0.0018109999999999966
86543
0.0012211000000000027
86543
Сложность всех трех решений одинаковая.
Так как в первый и второй вариант решения идентичен и меняется только класс через который мы работаем.
Можно сделать вывод что операции со строками немного затратнее и не стоит их использовать если есть
математического решение.
'''