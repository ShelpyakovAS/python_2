"""
2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)
"""

num1 = list(str.upper(input('Введиете число: ')))
num2 = list(str.upper(input('Введиете число: ')))

list_of_numbers = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
if len(num1) > len(num2):
    first, second = num2, num1
num1.reverse()
num2.reverse()
num3 = []
k = 0
j = 0
for i in num2:
    one = list_of_numbers.index(i)
    two = list_of_numbers.index(num1[j])
    num3.append(list_of_numbers[(one + two + k) % 16])
    if (one + two) >= 15:
        k = 1
    else:
        k = 0
    j += 1
    if j == len(num1):
        break
diff = len(num2) - len(num1)
if diff:
    for i in num2[-diff:]:
        num3.append(list_of_numbers[(list_of_numbers.index(num2[-diff]) + k) % 16])
        if list_of_numbers.index(num2[-diff]) + 1 >= 15:
            k = 1
        else:
            k = 0
if k == 1:
    num3.append('1')

num3.reverse()
print(num3)
