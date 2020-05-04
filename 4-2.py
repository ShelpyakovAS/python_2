"""
Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
import timeit


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


def no_eratosthenes(i):
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n


def eratosthenes1(i):
    n = 2
    l = 10000
    sieve = [x for x in range(l)]
    sieve[1] = 0
    while n < l:
        if sieve[n] != 0:
            m = n*2
            while m < l:
                sieve[m] = 0
                m += n
        n += 1
    return [p for p in sieve if p != 0][i-1]

print(timeit.timeit("no_eratosthenes(10)", setup="from __main__ import no_eratosthenes", number=100))
print(f'{no_eratosthenes(10)}')
print(timeit.timeit("eratosthenes(10)", setup="from __main__ import eratosthenes", number=100))
print(f'{eratosthenes(10)}')
print(timeit.timeit("eratosthenes1(10)", setup="from __main__ import eratosthenes1", number=100))
print(f'{eratosthenes1(10)}')
print(timeit.timeit("no_eratosthenes(100)", setup="from __main__ import no_eratosthenes", number=100))
print(f'{no_eratosthenes(100)}')
print(timeit.timeit("eratosthenes(100)", setup="from __main__ import eratosthenes", number=100))
print(f'{eratosthenes(100)}')
print(timeit.timeit("eratosthenes1(10 )", setup="from __main__ import eratosthenes1", number=100))
print(f'{eratosthenes1(100)}')
print(timeit.timeit("no_eratosthenes(1000)", setup="from __main__ import no_eratosthenes", number=100))
print(f'{no_eratosthenes(1000)}')
print(timeit.timeit("eratosthenes(1000)", setup="from __main__ import eratosthenes", number=100))
print(f'{eratosthenes(1000)}')
print(timeit.timeit("eratosthenes1(1000)", setup="from __main__ import eratosthenes1", number=100))
print(f'{eratosthenes1(1000)}')

'''
0.0026018999999999973       Без использования «Решета Эратосфена» до 10 i 100 раз
29
0.0021051000000000056       Используя мой алгоритм «Решето Эратосфена» до 10 i 100 раз
29
0.5140302                   Используя алгоритм «Решето Эратосфена» до 10 i 100 раз
29
0.28491980000000006         Без использования «Решета Эратосфена» до 100 i 100 раз
541
0.13445619999999991         Используя мой алгоритм «Решето Эратосфена» до 100 i 100 раз
541
0.5125776999999999          Используя алгоритм «Решето Эратосфена» до 100 i 100 раз
541
46.315889999999996          Без использования «Решета Эратосфена» до 1000 i 100 раз
7919
16.548000399999992          Используя мой алгоритм «Решето Эратосфена» до 1000 i 100 раз
7919
0.5100721999999962          Используя алгоритм «Решето Эратосфена» до 1000 i 100 раз
7919
Алгаритм «Решето Эратосфена» эфективен при поиске числа с большим порядковым номером.
сложность Без использования «Решета Эратосфена» О(n^2)
сложность моего алгоритма «Решето Эратосфена» О(n^2 log n)
сложносьт алгоритм «Решето Эратосфена» O(n log(log n))
'''