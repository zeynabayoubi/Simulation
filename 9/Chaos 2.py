import numpy as np
import matplotlib.pyplot as plt

def population(r):
    P =  np.random.uniform(0,1,(1,100))
    for i in range (10000):
        P[:] = 4*r*P[:]*(1-P[:])
    return P


r = np.arange(0,1,0.001)
pop = np.zeros((len(r),100))
for i in range (len(r)):
    pop[i][:] = population(r[i])
    if(i%1000 == 0):
        print ("nana")

popplot = np.zeros((100 , len(r)))

for i in range (100):
    for j in range (len(r)):
        popplot[i][j] = pop[j][i]

for i in range (100):
    plt.scatter(r , popplot[i]  , c ='black'  )
#plt.xlim(0.6,0.8)
#plt.ylim(0.4, 0.6)
plt.xlabel("r")
plt.ylabel("x_infinite")

x = np.zeros(len(r))
x[:] = 0.5
plt.plot(r , x , c='red')
plt.show()
