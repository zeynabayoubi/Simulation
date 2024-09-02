import numpy as np
import random as rn
import matplotlib.pyplot as plt

def Y(N):

    random_array = np.random.randint(10,size = (N,100000) )

    y = np.zeros(100000)

    for i in range (100000):
        
        for j in range (N):


            y[i] += random_array [j][i]
        
        y[i] = y[i] / N
    
    return y


    
N = 5
y = Y(N)
n, bins, patches = plt.hist(y, bins=70, facecolor = 'r'  ,alpha=0.7, rwidth=0.85 , density=True)

N = 10
y = Y(N)
n, bins, patches = plt.hist(y, bins=70, facecolor = 'y' , alpha=0.7, rwidth=0.85 , density=True)

N = 100
y = Y(N)
n, bins, patches = plt.hist(y, bins=70, facecolor = 'g' , alpha=0.7, rwidth=0.85 , density=True)

N = 1000
y = Y(N)
n, bins, patches = plt.hist(y, bins=70, facecolor = 'b' , alpha=0.7, rwidth=0.85 , density=True)

plt.legend([ "N=5" , "N=10" , "N=100" , "N=1000" ])
plt.title ('Probability Density Distribution Function')
plt.show()
