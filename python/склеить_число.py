def ckl_chislo(lst):
    'СКЛЕИТЬ ЧИСЛО'
    if len(lst)== 0:
        return -1
    else:
        a =[str(i) for i in lst]
        chislo = ''.join(sorted(a, key =lambda z: tuple(z + z*100), reverse= True))
        return int(chislo)
print(ckl_chislo([7, 71, 72]))
print(ckl_chislo.__doc__)