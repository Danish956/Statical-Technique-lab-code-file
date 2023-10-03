import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,10,30)
y = x**2
z = x**3
plt.plot(x,z, color='red')
plt.plot(x, y, '*')
plt.xlabel('x - values')
plt.ylabel('y - values')
plt.title('line plot')
plt.grid(True)
plt.show()

