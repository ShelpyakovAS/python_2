"""
Закодируйте любую строку из трех слов по алгоритму Хаффмана.

Пример:
строка для кодирования
s = "beep boop beer!"

Результат:
00 11 11 101 010 00 011 011 101 010 00 11 11 1000 1001
"""
import operator

line = 'beep boop beer!'

list_line = []

for i in line:
    list_line.append(i)

line_dict = {}
for i in list_line:
    line_dict.update({i: list_line.count(i)})

sorted_x = sorted(line_dict.items(), key=operator.itemgetter(1))

print(sorted_x)












