lst = input().split()
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
print(lst, lst1)
te_xt = lst2
c,e = [],[]
for i in range(len(te_xt)):
    for j in te_xt[i]:
        sag = len(lst1[i])
        if j.isalpha():
            b = ord(j) + sag
            if b > 122:
                c.append(chr(b - 26))
            elif b < 96:
                c.append(chr(b + 26))
            else:
                c.append(chr(b))
        else:
            c += j
    e.append(c)
    c = []

print(e)
for i in range(len(lt)):
    for j in range(len(lt[i])):
        if lt[i][j] == lt[i][j].upper():
            e[i][j] = e[i][j].upper()
        else:
            e[i][j] = e[i][j].lower()
for i in e:          
    print(''.join(i), end=' ')
