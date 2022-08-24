def pascal(n):
    lst = []
    for i in range(n+1):
        elem = [1]*(i+1)
        for j in range(i+1):
            if j != i and j != 0:
                elem[j] = lst[i-1][j-1]+lst[i-1][j]
        lst.append(elem)
    if n == 0:
        return [1]
    else:
        return lst


n = int(input())
print(*pascal(n), sep='\n')
