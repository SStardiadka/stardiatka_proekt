# библиотеки_питона


#  functools
items = [1, 2, 3, 4, 5]
sum_all = __import__('functools').reduce(lambda x,y: x * y, items)
sum_all
# 150