# Задача 16. Задайте список из n чисел последовательности 
# 〖(1+1/n)〗^n  и выведите на экран их сумму.

num = input("Введите натуральное число n: ")
try:
    tmp = int(num)
except:
    print('Введенное значение не является натуральным числом')
    exit()
if int(num) < 0:
    print('Введенное чмсло является отрицательным')
    exit()

list = []
sum = 0
for i in range(1, int(num) + 1):
    elem_n = (1 + 1/i) ** i   
    sum += elem_n    
    list.append(elem_n)    
print(f'Заданная последовательность 〖(1+1/n)〗^ n от 1 до {num} имеет вид: \n {list}')
print(f'Сумма элементов данной последовательности составляет: {sum}')