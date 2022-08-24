a=float(input())
b=float(input())
c=input()
if c=='/'and b==0:
    print("Деление на 0!")
elif c=='/'and b!=0:
    print(a/b)
elif c=='*':
    print(a*b)
elif c=='-':
    print(a-b)
elif c=='+':
    print(a+b)
elif c=='mod'and b==0: #mod — это взятие остатка от деления (%)
    print("Деление на 0!")
elif c=='mod'and b!=0:
    print(a%b)
elif c=='div'and b==0: #div — целочисленное деление (//)
    print("Деление на 0!")
elif c=='div'and b!=0:
    print(a//b)
elif c=='pow':         #pow — возведение в степень,(**)
    print(a**b)
