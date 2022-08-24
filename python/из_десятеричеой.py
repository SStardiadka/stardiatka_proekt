# перевести в любую из десятеричеой
def translate(x,n = 2):
    l=[]
    while x > 0:
        res = x % n
        x //= n
        l.insert(0,str(res))
    return int(''.join(l))

print(translate(int(input())))

