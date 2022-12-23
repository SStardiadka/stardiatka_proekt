# рисует круговую диограмму
from cProfile import label
import matplotlib.pyplot as plt

class Grafik_kryg:
    def __init__(self, q1='Россия', q2='Беларусь', q3='Москва', q4='Минск'):
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.q4 = q4
    
    def risyet(self, te=50, tq = 20, tw =10, tr=5):
        self.te = te
        self.tq = tq
        self.tw = tw
        self.tr = tr
        labels =[self.q1, self.q2, self.q3, self.q4]
        valyes =[te, tq, tw, tr]

        plt.pie(valyes, labels = labels)
        plt.axis('equal')
        plt.show()

res = Grafik_kryg()
res.risyet()