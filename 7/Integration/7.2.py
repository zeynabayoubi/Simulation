import numpy as np
from time import time

#R = 2

def ro(r , teta):
    return ((r*np.cos(teta))/2 + 3 ) / 4

def f(r , teta ):
    return ro(r , teta) * (r*np.cos(teta)) * (r**2 * np.sin(teta))

def M(r , teta ):
    return ro(r , teta) * (r**2 * np.sin(teta))
    
t0 = time()
N = 10000000
r = np.random.uniform(0,2,(1,N))
teta = np.random.uniform(0,np.pi,(1,N))
#phi = np.random.uniform(0,2 * np.pi,(1,N))

f_array = np.zeros((1,N))
M_array = np.zeros((1,N))
f_array[:] = f(r[:] , teta[:] )
M_array[:] = M(r[:] , teta[:] )
f_mean = np.mean(f_array)
M_mean = np.mean(M_array)

Integrate_f = 4 * (np.pi)**2 * f_mean
Integrate_M = 4 * (np.pi)**2 * M_mean
t1 = time()

print("Center of mass = ", Integrate_f / Integrate_M  )
print("runtime = " , t1-t0)
