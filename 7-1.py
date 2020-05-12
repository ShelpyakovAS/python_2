"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).
Идея доработки: если за проход по списку не совершается ни одной сортировки, то завершение
Обязательно сделайте замеры времени обеих реализаций

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""
import random
import timeit


def bubble_sort(orig_list):
    n = 1
    while n < len(orig_list):
        for i in range(len(orig_list)-n):
            if orig_list[i] < orig_list[i+1]:
                orig_list[i], orig_list[i+1] = orig_list[i+1], orig_list[i]
            else:
                n = len(orig_list)
        n += 1
    return orig_list

orig_list = [random.randint(-100, 100) for i in range(10)]
# замеры 10
print(timeit.timeit("bubble_sort(orig_list)", setup="from __main__ import bubble_sort, orig_list", number=1000))
print(orig_list)
orig_list = [random.randint(-100, 100) for i in range(100)]

# замеры 100
print(timeit.timeit("bubble_sort(orig_list)", setup="from __main__ import bubble_sort, orig_list", number=1000))
print(orig_list)
orig_list = [random.randint(-100, 100) for i in range(1000)]

# замеры 1000
print(timeit.timeit("bubble_sort(orig_list)", setup="from __main__ import bubble_sort, orig_list", number=1000))
print(orig_list)
'''
До оптимизации
0.011843300000000005
0.7162906
67.7387493

После оптимизации
0.0027708000000000003
0.0188596
0.2695362
'''