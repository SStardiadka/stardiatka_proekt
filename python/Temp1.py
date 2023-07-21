# import emoji 
# print(emoji.emojize('Python is :thumbsup:', language='alias'))
# # Python is 👍
# print(emoji.emojize('Python is :thumbs_up:'))
# # Python is 👍
lst = [1, 2, 3, 4, 5, 6, 7, 8]
n = 0
while n < 8:
    a = lst.pop(0)
    dk ={str(a):str(n)}
    lst.append(dk)
    n += 1
print(lst)