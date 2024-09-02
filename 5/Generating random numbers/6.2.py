import numpy as np
import random as rn
import matplotlib.pyplot as plt

def creating_the_random_numbers(N):
    Distribution_array = np.zeros(10)

    for i in range (N):
        c = rn.randint(0,9)
        if c==4:
            d = rn.randint(0,9)
            Distribution_array[d]+=1
    return Distribution_array


y = creating_the_random_numbers(10000)
w = np.std(y)
print(w)
print(y )

x = np.arange(0,10)
plt.bar(x , y , color="mediumvioletred" , edgecolor='black')
plt.title("Distribution Diagram")
plt.xticks(x)
plt.show()
