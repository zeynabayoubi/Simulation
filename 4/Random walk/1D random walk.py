import random as rn
import numpy as np
import matplotlib.pyplot as plt



def One_dimensional_random_walk (N , p):
    the_array_of_position = np.zeros((1000,N+1))
    
    for i in range (1000):
        x = 0
        for j in range (N):
            c = rn.random()
            if c<= p:
                x = x+1
            else:
                x = x-1
            the_array_of_position[i][j+1]=x  

    return the_array_of_position

def Analizing_data (the_array_of_position , N):

    mean_value_of_x = np.zeros(N+1)
    mean_value_of_x2 = np.zeros(N+1)
    Sigma2 = np.zeros(N+1)
    
    for i in range (N):
        for j in range (1000):
            mean_value_of_x[i+1] += the_array_of_position[j][i+1]
            mean_value_of_x2[i+1] += (the_array_of_position[j][i+1])**2

    mean_value_of_x = mean_value_of_x / 1000
    mean_value_of_x2 = mean_value_of_x2 / 1000
    Sigma2[:] =  mean_value_of_x2[:] -  (mean_value_of_x[:])**2

    return mean_value_of_x , mean_value_of_x2 , Sigma2


#main code:

N = int ( input ("Enter the number of steps: "))
p = float ( input ("Enter the probability of walking in right hand: "))

#l=1 , tau =1


the_array_of_position = One_dimensional_random_walk (N , p)
mean_value_of_x , mean_value_of_x2 , Sigma2 =  Analizing_data(the_array_of_position , N)

t = np.arange(0,N+1)
plt.scatter(t , Sigma2)
plt.xlabel('time')
plt.ylabel('sigma^2')
plt.show()

m , b = np.polyfit(t , Sigma2 , 1)
print(m)
print(4*p*(1-p))

    
