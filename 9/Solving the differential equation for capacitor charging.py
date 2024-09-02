import numpy as np
import matplotlib.pyplot as plt

# Analytic solution: Q`(tau) = 1-exp(-tau)  or  Q(t) = VC(1-exp(-t/RC)
def Analytic_solution(tau):
    return 1-np.exp(-tau)

t = np.arange(0,7,0.1)
Q_Analytic = np.zeros(len(t))
Q_Analytic[:] = Analytic_solution(t[:])
#plt.scatter(t , Q_Analytic)
plt.plot(t , Q_Analytic)



Q = np.zeros(len(t))

q = 0
h = 0.0001

#dQ/dt = 1 - Q

for i in range (7*int(1/h)):
    q = ( q + h * (1-q) )
    if (i+1)%1000 == 0:
        if int((i+1)/1000)<70:
            Q[int((i+1)/1000)] = q

plt.scatter(t , Q , c='red')
#plt.plot(t , Q)
plt.xlabel("t(*0.003) [s]")
plt.ylabel("Q(t)(*e-5) [C]")
plt.legend(["Analytic solution" , "Euler Metod"])
plt.show()

#Calcuting the relative error for different h:
#h = np.arange(0.00001 , 0.1 ,0.0001)
h = np.logspace(-7 , -1 , 100)


relative_error = np.zeros(len(h))

for i in range (len(h)):
    t = np.arange(0,7,(h[i]))
    q = 0
    p = 0
    for j in range (len(t)):
        q = ( q + (h[i]) * (1-q) )
        
    relative_error[i] = abs(q - Analytic_solution(t[len(t)-1]))/Analytic_solution(t[len(t)-1])

plt.scatter(h , relative_error )
plt.xlabel('h(*0.003) [s]')
plt.ylabel('delta(Q)/Q')
plt.xscale('log')
plt.yscale('log')
plt.show()

m , b = np.polyfit(np.log(h) , np.log(relative_error) , 1)
print("m = " , m)
    
