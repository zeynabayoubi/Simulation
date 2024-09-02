import numpy as np
import matplotlib.pyplot as plt

def census (t_max , x0 , p , q):

    main_array = np.zeros(( t_max , (2*t_max)+4*x_trap ))

    main_array[0][int(((2*t_max)+4*x_trap)/2) +x0 ] = 1 #initial condition

    for i in range (1 , t_max):
        for j in range ( (2*t_max)+4*x_trap -1 ):
                main_array[i][j] = (main_array[i-1][j-1])*p + (main_array[i-1][j+1])*q
    
    return main_array


def death (main_array , x_trap , t_max ):
    probability_of_death_in_time_t = np.zeros(t_max)
    x_center = int ( (2*t_max +4*x_trap)/2 )
    

    for i in range (t_max):
        summation=0
        for j in range (0, x_center - x_trap):
            summation += main_array[i][j]
        for j in range (x_center + x_trap +1, (2*t_max)+4*x_trap):
            summation += main_array[i][j]
      

        probability_of_death_in_time_t[i] = summation


   
    return probability_of_death_in_time_t


def mean_time_of_death (probability_of_death_in_time_t  , t_max):
    mean_time_of_death = 0
    for i in range (t_max):
        mean_time_of_death += i*probability_of_death_in_time_t[i]

    sum1=0
    for i in range (t_max):
        sum1 += probability_of_death_in_time_t[i]
    probability_of_death_in_time_t = probability_of_death_in_time_t / sum1

    mean_time_of_death = mean_time_of_death / sum1
    
    return mean_time_of_death

#main code:

X0 = np.arange(-10,+11)
x_trap = 11
p = float(input("Enter the probability of walking in right hand: "))
q = 1-p
t_max = 200
t_death = np.zeros(21)

for i in range (21):
    main_array = census (t_max , X0[i] , p , q)
    probability_of_death_in_time_t = death (main_array , x_trap , t_max )        
    T =  mean_time_of_death (probability_of_death_in_time_t  , t_max)
    t_death[i] = T
            
plt.scatter(X0 , t_death)
plt.xlabel('X0')
plt.ylabel('mean time of death')
plt.show()
        
    
    
