import numpy as np
import random as rn
import matplotlib.pyplot as plt

def Y(N):

    y = np.zeros(1000000)

    for i in range (1000000):

        for j in range (N):

            c = rn.randint(0,9)

            y[i] += c
        
        y[i] = y[i] / N
    
    return y


N = 10
y = Y(N)

n, bins, patches = plt.hist(y, bins=70, color='#0504aa',alpha=0.7, rwidth=0.85 , density=True)
plt.title ('Probability Density Distribution Function')
plt.show()
