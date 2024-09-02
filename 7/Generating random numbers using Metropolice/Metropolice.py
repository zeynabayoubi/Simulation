import numpy as np
import random as rn
import matplotlib.pyplot as plt

def p(x):
    return np.exp(-x**2)

def C(L , N):
    C = np.zeros(25)
    
    sigma2 = np.var(L)
    for k in range(1,26):
        C[k-1] = ( np.mean(L[:-k]*L[k:]) - np.mean(L[:-k])*np.mean(L[k:]) )/sigma2
    return C

N = 1000000
x = 0
accept = 0
L = []
L.append(x)

Delta = float(input("Enter the length of the step: "))



for k in range(N):
    s  = np.random.uniform(-1,1)
    
    y = x + Delta * s
        
    w = min(1 , p(y)/p(x))
    c = rn.random()
    if c<=w:
        x=y
        accept += 1
        L.append(x)
L = np.array(L)

acceptance_rate = accept / N
print('acceptance rate = ' , acceptance_rate)
plt.hist(L ,  bins=70, facecolor = 'g' , alpha=0.7, rwidth=0.85 , density=True)
plt.xlabel('x')
plt.ylabel('density of p(x)')
plt.show()

C1 = C(L , N)

j = np.arange(1,26)
plt.plot(j , C1)
plt.title('C(j) Diagram')
plt.show()

plt.plot(j , np.log(C1))
plt.title('ln(C(j)) Diagram')
plt.show()
m , b = np.polyfit(j , np.log(C1) , 1)
print('length of correlation = ',-(1/m))

length_of_correlation = [1,1,1,1,1,2,3,6,23]
acceptance_rate = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
plt.scatter(acceptance_rate , length_of_correlation)
plt.xlabel('acceptance rate')
plt.ylabel('length of correlation')
plt.show()


    
