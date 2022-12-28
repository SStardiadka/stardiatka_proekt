def text_decor(funk):
    def init(*args, **kwargs):
        funk(*args, **kwargs)
        for i in args:
            i = i * 10
            yield args
    return init
@text_decor
def simple_func(*args):
    for i in args:
        print(i)

for i in simple_func(3, 5, 7, -1):
    print(i)

# Вывод
# Hello
# I just simple python func
# Goodbye!