#  число в десятиричное
chislo = input()
n = int(input('разряд числа'))
j = 0
s = 0
for i in range(len(chislo) -1, -1, -1):
    s += int(chislo[j]) * n**i
    j += 1
print(s)