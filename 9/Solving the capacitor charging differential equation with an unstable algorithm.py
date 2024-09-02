import numpy as np
import matplotlib.pyplot as plt

# Analytic solution: Q`(tau) = 1-exp(-tau)  or  Q(t) = VC(1-exp(-t/RC)
def Analytic_solution(tau):
    return 1-np.exp(-tau)

for h in [0.08 , 0.1 ]:
    t = np.arange(0,8,h)

    Q = np.zeros(len(t))
    q0 = 0
    q1 = Analytic_solution(t[1])
    Q[1] = q1

    for i in range (int(8/h) -2 ):
        q = q0 + 2*(1-q1)*h
        Q[i+2] = q
        q0 = q1
        q1 = q
        
    plt.plot(t , Q )



Q_Analytic = np.zeros(len(t))
Q_Analytic[:] = Analytic_solution(t[:])
plt.plot(t , Q_Analytic , 'green')

plt.xlabel("t(*0.003) [s]")
plt.ylabel("Q(t)(*e-5) [C]")

plt.legend([ "h = 0.08" , "h = 0.1" , "Analytic solution" ])
plt.show()
