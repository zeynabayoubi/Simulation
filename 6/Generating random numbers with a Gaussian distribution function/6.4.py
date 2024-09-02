import numpy as np
import random as rn
import matplotlib.pyplot as plt

x1 = np.random.uniform(0,1,(1,1000000))
x2 = np.random.uniform(0,1,(1,1000000))

#sigma2 = 1/2

ro = np.zeros(1000000)
ro[:] = (- np.log(x2[:]))**(1/2)

teta = np.zeros(1000000)
teta[:] = 2*(np.pi)*x1[:]

y1 = np.zeros(1000000)
y2 = np.zeros(1000000)

y1[:] = ro[:] * np.cos(teta[:])
y2[:] = ro[:] * np.sin(teta[:])



n, bins, patches = plt.hist(y2, bins='auto', color='#0504aa' , alpha=0.7, rwidth=0.85 , density=True)
plt.title ('Probability Density Distribution Function')
plt.show()


