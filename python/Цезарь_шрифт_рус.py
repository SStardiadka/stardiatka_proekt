def new_func():
    lst = input().split() # шифр цезаря руский со здвигом и 
#  сохранением больших и малых букв и знаков припинания
    a, lt = [],[]
    for i in lst:
        for j in i:
            a.append(j)
        lt.append(a)
        a = []
        
    lst1 =[i for i in lst]
    lst2 =[i.lower() for i in lst]
    for i in range(len(lst1)):
        lst1[i] = lst1[i].strip(".\",;:-?!")

    te_xt = lst2
    c,e = [],[]
    sag = -7
    for i in range(len(te_xt)):
        for j in te_xt[i]:
            if j.isalpha():
                b = ord(j) + sag
                if b > 1103:
                    c.append(chr(b - 32))
                elif b < 1071:
                    c.append(chr(b + 32))
                else:
                    c.append(chr(b))
            else:
                c.append(j)
        e.append(c)
        c = []

    for i in range(len(lt)):
        for j in range(len(lt[i])):
            if lt[i][j] == lt[i][j].upper():
                e[i][j] = e[i][j].upper()
            else:
                e[i][j] = e[i][j].lower()
    for i in e:          
        print(''.join(i), end=' ')

new_func()
