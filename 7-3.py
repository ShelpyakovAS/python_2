"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках
"""
import random


m = random.randint(1, 10)
orig_list = [random.randint(-1000, 1000) for i in range(2*m + 1)]
orig_list2 = sorted(orig_list)  # это для наглядности
print(orig_list2)
if len(orig_list) == 1:
    median = orig_list[0]
    print(f'Медиана массива равна: {median}')
else:
    median = int((max(orig_list)+min(orig_list))/2)
    right = 0
    left = 0
    n = False
    while n == False:
        if median in orig_list:
            n = True
        else:
            median += 1
    while n != False:
        right = 0
        left = 0
        near_right = 1000
        near_left = -1000
        for i in orig_list:
            if near_left < i < median:
                near_left = i
            elif median < i < near_right:
                near_right = i
            if i < median:
                left += 1
            elif i > median:
                right += 1
            elif i == median:
                right += 0.5
        right = int(right)
        if right == left:
            print(f'Медиана массива равна: {median}')
            n = False
        elif left > right:
            median = near_left
        else:
            median = near_right


'''Не будет работать если медиана повторяется в массиве больше 2х раз'''

