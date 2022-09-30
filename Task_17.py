# Задача 17.	Задайте число N, создайте список: [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции (случайные)  хранятся в файле file.txt
# (создаётся во время выполнения кода и зависит от количества элементов в списке)
# в одной строке одно число

import random
num = input("Введите натуральное число N: ")
try:
    tmp = int(num)
except:
    print('Введенное значение не является натуральным числом')
    exit()
if int(num) < 0:
    num = abs(int(num))

list = []
for i in range(-int(num), int(num)+1):
    list.append(i)
print(f'Список элементов от числа -{num}  до {num}: {list}')

i = 0
position = []
while i < int(num):
    number = random.randint(0, len(list))
    position = position + [number]
    i = i+1
print("Позиция элеменитов списка для записи в файл:  ", position)

with open('file.txt', 'wt') as File: # Открытие файла для записи (если файла нет - будет создан)
    for i in position:
        pos = str(i)
        File.write(pos + '\n')

with open('file.txt', 'rt') as File: # Открытие файла для чтения
    position_text = []
    for line in File:
        pos_text = int(line)
        position_text.append(pos_text)
print("Позиция элеменитов списка, прочитанная из файла:  ", position_text)
File.close()

mult = 1
for i in range(len(position_text)):
    elem = position_text[i] 
    mult *= list[elem]
    print(list[elem])  # для проверки, после тестирования убрать   
print(f'Произведение элементов списка от -{num}  до {num} на данных позициях равно: {mult}')

