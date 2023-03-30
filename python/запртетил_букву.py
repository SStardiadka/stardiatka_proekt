# запртетил_букву
def zapret_bykvi(name):
    alf = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    str = name + " запретил букву"
    lst = []
    for i in alf:
        if i in str:
            lst.append(str + " " + i + "\n")
            str = str.replace(i, "")
            str = " ".join(str.split())
    a = "".join(lst)
    return a


print(zapret_bykvi("роскомнадзор"))
zapret_bykvi.__class__
