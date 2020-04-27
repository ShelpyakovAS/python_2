"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""
from random import random

def guess_number(answer, number_try=10):
    if number_try > 0:
        user_answer = int(input(str(number_try) + '-я попытка: '))
        if user_answer > answer:
            print('Много')
        elif user_answer < answer:
            print('Мало')
        else:
            print(f'Вы угадали с {str(number_try)}-й попытки')
            return
        return guess_number(answer, number_try-1)
    else:
        print(f'Вы исчерпали 10 попыток. Было загадано число {answer}')

answer = round(random() * 100)
print("Компьютер загадал число. Отгадайте его. У вас 10 попыток")
guess_number(answer)