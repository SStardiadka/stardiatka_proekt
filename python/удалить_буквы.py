def replase_bykvi(str):
    a = ''
    for i in str:
        if i.isalpha():
            a = a + ' '
        else:
            a = a + i
