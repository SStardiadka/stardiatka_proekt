def convert(L):  # индекс максимальной цифры числа
    return [int(i) for i in L]

def maxId(L):
    L = convert(L)
    return(L.index(max(L)))
