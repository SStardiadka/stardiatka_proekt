files = open(r'C:\Users\user\Desktop\dataset_3380_5 (2) — копия.txt', encoding='utf-8')
text = files.readlines()
a = []
b = []
files.close()
text = [i.replace('\t', ',').rstrip() for i in text]
text = [i.split(',') for i in text]
a = [[] for _ in range(12)]
for i in range(len(a)):
    for j in range(len(text)):
        if i == int(text[j][0]):
            a[i].append(text[j][-1])
for i in range(1, 12):
    if len(a[i]) == 0:
        print(f'{i} -')
    else:
        print(f'{i} {sum(map(int, a[i])) / len(a[i])}')
