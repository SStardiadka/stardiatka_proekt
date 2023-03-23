#  число в десятиричное
def new_func(chislo, n):
    j = 0
    s = 0
    for i in range(len(chislo) - 1, -1, -1):
        s += int(chislo[j]) * n**i
        j += 1
    print(s)


chislo = input()
n = int(input())

new_func(chislo, n)
