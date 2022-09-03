def n_str_matrix(n):   
    'список  квадратной матрицы из n строк'
    matrix = []
    for i in range(n):
        temp = [int(num) for num in input().split()]
        matrix.append(temp)
    return(matrix)

print(n_str_matrix.__doc__)

