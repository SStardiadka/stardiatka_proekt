#  генератор прароля
from random import randint as ri
length = int(input())    # длина пароля
for i in range(length):
    num = ri(65, 90)
    num1 = ri(97, 122)
    dict1 = {1: num, 2: num1}
    print(chr(dict1[ri(1, 2)]), end='')
