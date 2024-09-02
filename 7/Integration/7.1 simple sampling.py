import numpy as np
from time import time

def f(x):
    return np.exp(-x**2)



N = 1000000

t0 = time()
x = np.random.uniform(0,2,(1,N))
f_array = np.zeros((1,N))
f_array[:] = f(x[:])
f_mean = np.mean(f_array)
t1 = time()
    

mean_of_f = np.mean(f_array)
statistical_error = 2 * ((np.std(f_array))/(N**(1/2)))



print("Intgrate = ", 2 * mean_of_f )
print("runtime = "  , t1 - t0 )
print("statistical_error = " ,statistical_error)

