#  вершины_парабалы
def vertices_parabola(a, b, c):
    return round((-b / (2 * a)), 1), round(a * (-b / (2 * a))**2 + b * (-b / (2 * a)) + c, 1)


a, b, c = float(input()), float(input()), float(input())
print(vertices_parabola(a, b, c))
