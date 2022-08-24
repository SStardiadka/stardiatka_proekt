from math import *
#  площадь правильного многоугольника


def polygon_area(n, a):  # сторон n, длинна сторны а
    return (n * a**2) / (4 * tan(pi / n))


print(polygon_area(int(input()), float(input())))
