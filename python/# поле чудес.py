# поле чудес
a = ['л','о','т','о']
b = ['-','-','-', '-']
while '-' in b:
    c = input()
    for i, el in enumerate(a):
        if c == el:
            b[i]= c
    if '-' in b:
        print(b)
print(b)
