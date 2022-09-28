# 18.	Реализуйте алгоритм перемешивания списка

import random
from random import randint

lst = []
for i in range(10):
    lst.append(randint(-10, 10))
print(lst)

random.shuffle(lst)
print(lst)

# # получаем список цифр от 0 до 8
# x = list(range(0,9))
# print(x)
# # список `x` перемешивается "на месте"
# # т.е. новый список не возвращается
# random.shuffle(x)
# # [4, 6, 0, 7, 2, 3, 1, 8, 5]
# print(x)
