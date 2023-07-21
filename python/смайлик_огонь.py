a = [["\N{fire}" for i in range(5)] for j in range(5)]
for i in a:
    print(*i)
    """
    🔥 🔥 🔥 🔥 🔥
    🔥 🔥 🔥 🔥 🔥
    🔥 🔥 🔥 🔥 🔥
    🔥 🔥 🔥 🔥 🔥
    🔥 🔥 🔥 🔥 🔥
                """
for i in range(1, 31):
    # a = 90 // i
    # b =  120 // (i + 2)
    if 90 / i  == 120 / (i + 2):
        print(i, i + 2)
       
        print(f'пчела: \U0001F9BA {28 - i}')
        print(f'сердце: \N{Growing Heart} {i}')
        print(f'питон: \N{Snake} {i+2}')
        print(f'цыплёнок: \N{Baby Chick} {120 // (i + 2)}')
        '''
        6 8
        пчела: 🦺 22
        сердце: 💗 6
        питон: 🐍 8
        цыплёнок: 🐤 15
        '''
        
# def func(x):
#     intermediate_var = x**2 + x + 1

#     if intermediate_var % 2:
#         y = intermediate_var ** 3
#     else:
#         y = intermediate_var **3 + 1

#     # setting attributes here
#     func.optional_return = intermediate_var
#     func.is_awesome = 'Yes, my function is awesome.'

#     return y

# y = func(3)
# print('Final answer is', y)

# # Accessing function attributes
# print('Show calculations -->', func.optional_return)
# print('Is my function awesome? -->', func.is_awesome)
