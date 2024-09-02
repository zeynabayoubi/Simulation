import numpy as np
import random as rn
import matplotlib.pyplot as plt 

N = int(input("Enter N: "))

x = np.zeros(N)
y = np.zeros(N)

for i in range(1, N):
    c = rn.random()
      
    if c <= 0.01:
        x[i] = 0
        y[i] = 0.16 * y[i-1]
         
    elif c <= 0.86:
        x[i] = 0.85 * x[i-1] + 0.04*y[i-1]
        y[i] = -0.04 * x[i-1] + 0.85 * y[i-1] + 1.6 
      
    elif c <= 0.93: 
        x[i] = 0.2 *x[i-1] - 0.26*(y[i-1]) 
        y[i] = 0.23 * x[i-1] + 0.22 * y[i-1] + 1.6 
          
    elif c <= 1: 
        x[i] = -0.15 * x[i-1] + 0.28* y[i-1] 
        y[i] = 0.26 * x[i-1] + 0.24 * y[i-1] + 0.44

plt.scatter(x, y, s = 0.2, c ='#5dbb63') 
plt.axis("off")
plt.show()
