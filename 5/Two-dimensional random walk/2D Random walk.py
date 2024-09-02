import numpy as np
import matplotlib.pyplot as plt
import random as rn

def Two_dimensional_random_walk ():

    r2_array = np.zeros((1000 , 100))

    for i in range (1000):
        
        x = 0
        y = 0
    
        for j in range (100):
    
            c = rn.randint(1,4)
    
            if c==1 : #1 is up
                y+=1
                r2_array[i][j] = x**2 + y**2
                
            if c==2 : #2 is down
                y-=1
                r2_array[i][j] = x**2 + y**2

            if c==3 : #3 is right
                x+=1
                r2_array[i][j] = x**2 + y**2

            if c==4 : #4 is left
                x-=1
                r2_array[i][j] = x**2 + y**2

    return r2_array


def Analysis (r2_array):

    mean_r2 = np.zeros(100)

    for i in range (100):
        
        for j in range (1000):

            mean_r2[i] += r2_array [j][i]

        mean_r2[i] = mean_r2[i]/1000

    return mean_r2

        
#main code:

t = np.arange(1,101)
r2_array = Two_dimensional_random_walk ()
mean_r2 = Analysis (r2_array)

plt.scatter (t , mean_r2)
plt.plot (t , mean_r2)
plt.xlabel ("time (numbers of steps) ")
plt.ylabel ("mean of r^2")
plt.show()

m , b = np.polyfit (t , mean_r2 , 1)
print ("m= " , m)


            
        
        

    
        
        
