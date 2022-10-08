#  класс_строки
class Workstr:   
    
    def zapret_bykvi(self, name = 'Дима'):
        self.name = name
        alf = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        str = name + ' запретил букву'
        lst = []
        for i in alf:
            if i in str:
                lst.append(str + ' ' + i +'\n')
                str = str.replace(i, '')
                str= ' '.join(str.split())
        a = ''.join(lst)
        return a

zp = Workstr()
print(zp.zapret_bykvi())