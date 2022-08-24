sag, te_xt = int(input()), input(),
c = []
for i in range(len(te_xt)):
    b = ord(te_xt[i]) + sag
    if b > 122:
        c.append(b - 26)
    elif b < 96:
        c.append(b + 26)
    else:
        c.append(b)
for n in c:
    print(chr(n), end='')
