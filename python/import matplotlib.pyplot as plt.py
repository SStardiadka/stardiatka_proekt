
from cProfile import label
import matplotlib.pyplot as plt
import numpy as np
labels =['Россия','Беларусь', 'Москва', 'Минск']
valyes =[50, 20, 10, 5]

plt.pie(valyes, labels = labels)
plt.axis('equal')
plt.show()