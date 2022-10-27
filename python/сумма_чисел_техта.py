with open(r'C:\stardiatka_proekt\python\Rfiles\test.txt', encoding='utf-8') as files:
    text = files.read()
    
def replase_bykvi(str):
    a = 0
    for i, el in enumerate(str):
        if not  el.isdigit():
            str = str.replace(el, ' ')
    return sum([int(i) for i in str.split()])

print(replase_bykvi(text))
