"""
Задание 1.
Найти сумму и произведение цифр трехзначного числа,
которое вводит пользователь.

#print(124 // 100) = 1 - отбросить остаток
#print((124 // 10) % 10) = 2 - остаток от деления числа 12 на 10
#print(124 % 10) = 4 - остаток от деления числа 124 на 10

Пример: Целое трехзначное число 123
Сумма = 6
Произведение = 6

Подсказка: для получения отдельных цифр числа используйте арифм. операции
и НЕ ИСПОЛЬЗУЙТЕ операции с массивами
"""
a = int(input('Введите трехзначное число: '))
while a < 100 or a > 999:
    a = int(input('Вы ввели не трехзначное число!!! Введите трехзначное число: '))

print(f'Сумма цифр трехзначного числа {a} равна {(a // 100) + (a // 10) % 10 + (a % 10)}')
print(f'Произведение цифр трехзначного числа {a} равна {(a // 100) * ((a // 10) % 10) * (a % 10)}')