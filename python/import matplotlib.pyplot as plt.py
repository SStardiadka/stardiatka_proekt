import matplotlib.pyplot as plt
import numpy as np
name =['Россия','Беларусь', 'Москва', 'Минск']
valyes =[50, 20, 10, 5]
colors =['red','green','blue','yellow']
plt.pie(valyes, name = name, colors=colors)
plt.axis('equal')
plt.show()