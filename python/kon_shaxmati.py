matrix_zero = [[] * 8 for _ in range(8)]
mdl = ['8', '7', '6', '5', '4', '3', '2', '1']
mdl1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
horse1 = ' '.join(input())
horse = horse1.split(' ')
dot = []
p = mdl.index(horse[1])
pt = mdl1.index(horse[0])
for i in range(8):
    for j in range(8):
        if i == p and j == pt:
            matrix_zero[i].append('N')
        elif i == p - 1 and j == pt - 2 or i == p - 2 and j == pt - 1 or i == p - 2 and j == pt + 1 or i == p - 1 and j == pt + 2 or i == p + 1 and j == pt + 2 or i == p + 2 and j == pt + 1 or i == p + 2 and j == pt - 1 or i == p + 1 and j == pt - 2:
            matrix_zero[i].append('*')
        else:
            matrix_zero[i].append('.')
for k in matrix_zero:
    print(*k)
