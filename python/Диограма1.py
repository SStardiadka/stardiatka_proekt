import matplotlib.colors as colors
import matplotlib.pyplot as plt 
import numpy as np
   
  
values =[75, 300, 180, 37, 50, 75, 269, 125, 610, 830, 155, 220, 110, 240, 170, 300, 128, 120, 140, 310, 110, 250]
index = np.arange(22)
color = []
for i in values:
    if i > 0 and i < 50:
        color.append('black')
    if i >= 50 and i < 100:
        color.append('turquoise')
    if i >= 100 and i < 150:
        color.append('green')
    if i >= 150 and i < 200:
        color.append('yellow')
    if i >= 200:
        color.append('red')

plt.bar(index, values, color = color)

plt.grid()

plt.xticks(index + 0.4,['1', '3', '4', '5', '7', '8', '10', '12', '13', '14', '16', '17', '20', '22', '23', '24', '26', '27', '28', '29', '30', '31'])    
  
plt.ylabel('Сумма в рублях')   
plt.title('Цветы октябрь 2020')   

plt.show()