#  класс_строки
class Workstr:
    alf='абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    
    def __init__(self, stroka =' запретил букву'):
        self.stroka = stroka
    
    def zapret_bykvi(self, name ='дима'):
        str = name + self.stroka
        lst = []
        for i in self.alf:
            if i in str:
                lst.append(str + ' ' + i +'\n')
                str = str.replace(i, '')
                str= ' '.join(str.split())
        a = ''.join(lst)
        return a

zp = Workstr(' украл букву')
rec = zp.zapret_bykvi('тимур')
print(rec)