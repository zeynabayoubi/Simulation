import numpy as np
import random as rn
import matplotlib.pyplot as plt


def Distribution (N , random_array):
    Distribution_array = np.zeros(10)
    
    n = 0
    for i in range (int(N/100)):
        n += i*100
        
    for j in range ( n , n + N):
        Distribution_array[random_array[j]] += 1
        
    return Distribution_array


def mean_sigma(N , random_array):
    sigma = 0
    for i in range(100):
        y = Distribution (N , random_array[i])
        w = np.std(y)
        sigma += w
    sigma = sigma/100
    return sigma


#main code:

N = 100 * np.arange(1,11)
S = 0
for i in range (len(N)):
    S += N[i]

random_array = np.random.randint(10,size = (100,S) )
sigma_N = np.zeros(len(N))

for i in range (len(N)):
    sigma_N[i] = mean_sigma(N[i] , random_array)
sigma_N[:] = sigma_N[:] / N[:]

plt.scatter( np.log(N) , np.log(sigma_N) )
plt.xlabel('ln(N)')
plt.ylabel('ln(sigma/N)')

plt.show()
m , b = np.polyfit (np.log(N) , np.log(sigma_N) , 1)
print(m)
    



    
        
        
        
        

