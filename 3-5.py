"""
Задание_5.	В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию (индекс) в массиве.

Подсказка: максимальный отрицательный - элемент, наиболее близкий к нулю

Пример:
Базовый список: [-55, -69, -5, 72, -41, -58, -79, 58, 74, 1]
Максимальный отрицательный элемент в данном массиве = -5, его индекс 2
"""
a = [-55, -69, -5, 72, -41, -58, -79, 58, 74, 1]
number = min(a)
for i in a:
    if number < i < 0:
        number = i

print(f'Максимальный отрицательный элемент в данном массиве = {number}, его индекс {a.index(number)}')