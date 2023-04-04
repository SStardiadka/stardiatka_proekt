# рисует круговую диограмму
from cProfile import label
import matplotlib.pyplot as plt


class Grafik_kryg:
    def __init__(self, q1="Россия", q2="США", q3="Беларусь", q4="Китай"):
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.q4 = q4

    def risyet(self, te=46, tq=27, tw=1, tr=26):
        labels = [self.q1, self.q2, self.q3, self.q4]
        valyes = [te, tq, tw, tr]

        # fig, ax = plt.subplots()
        # fig.canvas.set_window_title("Население стран")
        plt.pie(valyes, labels=labels)
        # plt.set_aspect("equal")
        plt.axis("equal")
        plt.show()


res = Grafik_kryg()
res.risyet()
