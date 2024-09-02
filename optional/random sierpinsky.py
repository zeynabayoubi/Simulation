import numpy as np
import random as rn
import matplotlib.pyplot as plt

def middle_of_points ( point1 , point2 ):
    return ( (point1[0] + point2[0]) / 2 , ( point1[1] + point2[1] ) / 2 )

corners = [(0, 0), (0.5, 3**(0.5)/2), (1, 0)]

N = 100000
x = np.zeros(N)
y = np.zeros(N)

x[0] = rn.random()
y[0] = rn.random()

for i in range(1, N):
    j = rn.randint(0, 2) # random triangle vertex
    x[i], y[i] = middle_of_points( corners[j], (x[i-1], y[i-1]) )
    
plt.scatter(x, y, s=0.2)
plt.axis("off")
plt.show()
