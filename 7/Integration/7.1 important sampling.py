import numpy as np
from time import time

def f_g(x):
    return np.exp(-x**2) / np.exp(-x)

#g(x) = exp(-x)
#integrate of g(x) from x=0 to x=2 : 0.8647



N = 1000000

t0 = time()
x0 = np.random.uniform(0,0.8647,(1,N))
y = np.zeros(N)
y[:] = -(np.log(1-x0[:])) #y is a random array with distribution g(x)
f_g_array = np.zeros((1,N))
f_g_array[:] = f_g(y[:])
f_g_mean = np.mean(f_g_array)
t1 = time()
    

statistical_error = 0.8647 * ((np.std(f_g_array))/(N**(1/2)))



print("Intgrate = ", 0.8647 * f_g_mean )
print("runtime = "  , t1 - t0 )
print("statistical_error = " ,statistical_error)
