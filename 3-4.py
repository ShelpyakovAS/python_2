"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""
a = [-49, 26, 41, 75, 23, 52, 88, 60, 69, -18, 88, 88, 41, 88, 41]
number_count = 0
number = 0
for i in a:
    if a.count(i) > number_count:
        number_count = a.count(i)
        number = i

print(f'Число {number} встречается {number_count} раз.')
