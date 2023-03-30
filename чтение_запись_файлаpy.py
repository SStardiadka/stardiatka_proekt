with open(r"C:\Users\user\Desktop\dataset_3363_4 (7).txt", encoding="utf-8") as f:
    lst = [i.rstrip().split(";") for i in f.readlines()]
    ch = len(lst)
    lst1 = []
    s1, s2, s3 = 0, 0, 0
    for i in lst:
        lst1.append(sum([int(j) for j in i[1:]]) / 3)
        s1 += int(i[1])
        s2 += int(i[2])
        s3 += int(i[3])
    with open(
        r"C:\stardiatka_proekt-1\python\Wfiles\temp.txt", "w", encoding="utf-8"
    ) as file:
        for i in lst1:
            file.write(f"{i}\n")
        file.write(f"{s1/ch} {s2/ch} {s3/ch}")
    print(lst1)
    print(s1 / ch, s2 / ch, s3 / ch)
