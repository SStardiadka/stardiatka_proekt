s = str(input())
if s == ("прямоугольник"):
    a = float(input())
    b = float(input())
    print(a * b)
elif s == "круг":
    r = float(input())
    p=(3.14)
    print(p * (r ** 2))
elif s == "треугольник":
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c) / 2
    print((p * (p - a) * (p - b) * (p - c)) ** (1/2))






