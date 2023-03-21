import matplotlib.pyplot as plt
import numpy as np


class Diagrams:
    def __init__(self, lst1=[], lst2=[]):
        self.lst1 = lst1
        self.lst2 = lst2

    def crygovai(self):
        y = np.array(self.lst1)
        mylabels = self.lst2
        plt.pie(y, labels=mylabels)
        return plt.show()


kr = Diagrams([35, 25, 15, 10], ["земля", "марс", "меркурий", "луна"])
kr.crygovai()
