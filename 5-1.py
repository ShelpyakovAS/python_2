"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога

Предприятия, с прибылью ниже среднего значения: Копыта
"""

say_num = int(input('Введите количество предприятий для расчета прибыли: '))
sum_year_all = 0
min_sum = ''
max_sum = ''
for i in range(1, say_num+1):
    say_name = input('Введите название предприятия: ')
    say_money = input('через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ')
    sum_year = say_money.split(' ')
    sum_year = int(sum_year[0]) + int(sum_year[1]) + int(sum_year[2]) + int(sum_year[3])
    globals()['company' + str(i)] = (say_name, say_money, sum_year)
    sum_year_all += sum_year

for i in range(1, say_num+1):
    if sum_year_all / say_num > globals()['company' + str(i)][2]:
        min_sum = min_sum + ', ' + (globals()['company' + str(i)][0])
    else:
        max_sum = max_sum + ', ' + (globals()['company' + str(i)][0])


print(f'Средняя годовая прибыль всех предприятий: {sum_year_all / say_num}')
print(f'Предприятия, с прибылью выше среднего значения: {max_sum}')
print(f'Предприятия, с прибылью ниже среднего значения: {min_sum}')








