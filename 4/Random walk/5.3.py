import random as rn
import numpy as np
import matplotlib.pyplot as plt


def calcuting_time_of_daeth (x0 , p):
    x=x0
    N=0
    while x>-11 and x<11 :
        c = rn.random()
        if c<=p :
            x+=1
        else:
            x-=1
        N+=1
    time_of_death = N
    return time_of_death

def running (R , x0 , p):
    mean_time_of_death=0
    for i in range (R):
        N = calcuting_time_of_daeth (x0 , p)
        mean_time_of_death += N
    mean_time_of_death = mean_time_of_death / R
    return mean_time_of_death


#main code:

p = float(input("Enter the probability of walking in right hand: "))
R=1000

X0 = np.arange (-10,+11)
TIME_OF_DEATH = np.zeros(21)


for i in range (21):
    x0 = X0[i]
    mean_time_of_death = running(R , x0 , p)
    TIME_OF_DEATH[i] = mean_time_of_death
    

plt.scatter(X0 , TIME_OF_DEATH)
plt.xlabel('X0')
plt.ylabel('time of death')
plt.show()

