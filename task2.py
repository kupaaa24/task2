import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 100, 1000)  
y1 = np.sin(x)                  
y2 = np.exp(x / 20)              
y3 = np.log(x + 1)              


fig, ax1 = plt.subplots(figsize=(10, 6)) 


ax1.plot(x, y1, 'b-', label='sin(x)')
ax1.set_ylabel('sin(x)', color='b')
ax1.tick_params(axis='y', labelcolor='b')


ax2 = ax1.twinx()
ax2.plot(x, y2, 'r-', label='exp(x/20)')
ax2.set_ylabel('exp(x/20)', color='r')
ax2.tick_params(axis='y', labelcolor='r')


ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))  
ax3.plot(x, y3, 'g-', label='log(x + 1)')
ax3.set_ylabel('log(x + 1)', color='g')
ax3.tick_params(axis='y', labelcolor='g')


plt.title('Multiple Y-Axes Sharing a Common X-Axis with Large Data')


plt.show()
