with open(r'C:\Users\user\Desktop\lorem.txt', encoding="utf-8") as out:
    f = sum([i.upper().strip().split() for i in out], [])
    words ={}
    for i in f:
        words[i] = words.setdefault(i, 0) +1

    
    print(words)