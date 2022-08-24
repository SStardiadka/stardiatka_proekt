sag, te_xt = int(input()), input().lower()
c = []
for i in range(len(te_xt)):
    b = ord(te_xt[i]) - sag
    if b > 122 and te_xt[i].isalpha():
        c.append(b - 26)
    else:
        c.append(te_xt[i])
    if b < 96 and te_xt[i].isalpha():
        c.append(b + 26)
    else:
        c.append(te_xt[i])
    if 96 <= b <= 122 and te_xt[i].isalpha():
        c.append(b)
    else:
        c.append(te_xt[i])
for n in c:
    if int(n).isdisdigit():
        print(chr(n), end='')
    else:
        print(n, end='')
