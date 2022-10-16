
from cProfile import label
import matplotlib.pyplot as plt
import numpy as np
labels =['Россия','Беларусь', 'Москва', 'Минск']
valyes =[50, 20, 10, 5]
colors =['red','green','blue','yellow']
plt.pie(valyes, labels = labels, colors =colors)
plt.axis('equal')
plt.show()