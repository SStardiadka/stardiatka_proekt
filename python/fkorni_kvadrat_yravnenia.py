def find_the_roots(a, b, c):  # корни квадратного уравнения
    D = b**2 - (4 * a * c)
    if D < 0:
        return 'Нет корней'
    elif D == 0:
        return - (b / (2 * a))
    else:
        return (f'{((- b) - D**(1/2)) / (2 * a)}\n{((- b) + D**(1/2)) / (2 * a)}')


print(find_the_roots(float(input()), float(input()), float(input())))
