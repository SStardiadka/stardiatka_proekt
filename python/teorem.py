for a in range(1,151):
    for b in range(80,151):
        for c in range(100,151):
            for d in range(130,151):
                for e in range(140,151):
                    if a**5+b**5+c**5+d**5==e**5:
                        print(a+b+c+d+e)
                        print(a, b, c, d, e)
                        break
