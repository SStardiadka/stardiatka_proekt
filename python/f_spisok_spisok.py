def chunked(st, n):  # разбивает строку на 'n' элементов и влаживает их списком в список
    stl = st.split() 
    lst = []
    for i in range(n, len(stl)+1, n):
        lst.append(stl[i-n:i])
    if len(stl) % n == 0:
        return lst
    elif len(stl) % n != 0:
        lst.append(stl[-(len(stl) % n):])
        return lst


print(chunked(input(), int(input())))
