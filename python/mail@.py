#  регистрирует ник если его нету в базе, если есть предлагает другой
from datetime import datetime, date


class Mail:
    lst = []
    dk = {}
    s = 1
    
    def checking(self, nik):
        self.nik = nik
        if nik not in self.dk:
            self.lst.append((f'{nik}@Дмитрий.by {self.s} {date.today()} {datetime.now().time()}').split())
            self.s += 1
            print('OK')
            self.dk.setdefault(nik, 0)
        else:
            self.dk[nik] = self.dk.setdefault(nik, 0) + 1
            print(nik + str(self.dk[nik]))
    
    def nik_numer(self,numer):
        for i in self.lst:
            if numer == i[1]:
                print(f'Под номером {i[1]} зарегистрирован ник: {i[0]}')
            

res = Mail()
for i in range(int(input())):
    res.checking(input())
print()
print(res.dk)
print()
print(res.lst)
print()
res.nik_numer('2')

