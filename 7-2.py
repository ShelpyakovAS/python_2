"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
import random
import timeit


def merge_sort(orig_list):
    if len(orig_list) > 1:
        center = len(orig_list) // 2
        left = orig_list[:center]
        right = orig_list[center:]
        merge_sort(left)
        merge_sort(right)
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                orig_list[k] = left[i]
                i += 1
            else:
                orig_list[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            orig_list[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            orig_list[k] = right[j]
            j += 1
            k += 1
        return orig_list


n = int(input('Введите число элементов: '))
orig_list = [random.uniform(0, 50) for i in range(n)]
print(f'Исходный - {orig_list}')
print(f'Отсортированный - {merge_sort(orig_list)}')


'''
orig_list = [random.uniform(0, 50) for i in range(10)]
# замеры 10
print(timeit.timeit("merge_sort(orig_list)", setup="from __main__ import merge_sort, orig_list", number=1000))
print(orig_list)
orig_list = [random.uniform(0, 50) for i in range(100)]

# замеры 100
print(timeit.timeit("merge_sort(orig_list)", setup="from __main__ import merge_sort, orig_list", number=1000))
print(orig_list)
orig_list = [random.uniform(0, 50) for i in range(1000)]

# замеры 1000
print(timeit.timeit("merge_sort(orig_list)", setup="from __main__ import merge_sort, orig_list", number=1000))
print(orig_list)


0.020539
0.3176191
4.3135680999999995
'''