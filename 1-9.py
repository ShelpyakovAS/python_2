"""
Задание 9.	Вводятся три разных числа. Найти, какое из них является средним
(больше одного,  но меньше другого).

Подсказка: можно добавить проверку, что введены равные числа
"""
a = int(input('Первое число: '))
b = int(input('Второе число: '))
c = int(input('Третье число: '))

if a < b < c or c < b < a:
    print(f'Число {b} является средним!')
elif a < c < b or b < c < a:
    print(f'Число {c} является средним!')
elif b < a < c or c < a < b:
    print(f'Число {a} является средним!')
else:
    print('Введены равные числа')

