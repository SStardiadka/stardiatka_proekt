rows, cols = 3, 4           # rows - количество строк, cols - количество столбцов
#  по строкам
matrix = [[2, 3, 1, 0],
          [9, 4, 6, 8],
          [4, 7, 2, 7]]

for r in range(rows):
    for c in range(cols):
        print(matrix[r][c], end=' ')
    print()
# наоборот по столбцам
rows, cols = 3, 4           # rows - количество строк, cols - количество столбцов
print('              ')
matrix = [[2, 3, 1, 0],
          [9, 4, 6, 8],
          [4, 7, 2, 7]]

for c in range(cols):
    for r in range(rows):
        print(matrix[r][c], end=' ')
    print()
