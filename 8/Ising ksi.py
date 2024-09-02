import numpy as np
import random as rn
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def init():
    S = np.random.choice([-1,1],(L,L))
    return S


def energy (S , L , J):
    summation = 0
    for k in range (0,L):
        for m in range (0,L):
            summation += S[k][m] * S[(k-1)%L][m]
            summation += S[k][m] * S[(k+1)%L][m]
            summation += S[k][m] * S[k][(m-1)%L]
            summation += S[k][m] * S[k][(m+1)%L]
    summation = summation/2
    E_S = -(J * summation)
    return E_S/(2*L*L)

def delta_E (S , L , J , k , m):
    return 2*J*S[k][m]*(S[(k-1)%L][m] + S[(k+1)%L][m] + S[k][(m-1)%L] + S[k][(m+1)%L])

def magnetism (S , L):
    summation = 0
    for k in range (0,L):
        for m in range (0,L):
            summation += S[k][m]
    return summation/(L*L)

def Cv (E , L , beta):
    var_E = np.var(E)
    Cv = (beta**2) * (L*L) * var_E
    return Cv

def Ki (m , L , beta):
    var_m = np.var(m)
    ki = beta * (L*L) * var_m
    return ki
    

def montecarlo(L , N , beta):
    
    S = init()
    NVT = []
    NVT.append(S)
    for i in range (N):
        S = metropolice(L , S , beta)
        NVT.append(S)
        
    return NVT
    

def metropolice(L , S , beta):
    
    for k in range(L*L):
        
        i = rn.randint(0,L-1)
        j = rn.randint(0,L-1)

        S_new = np.zeros((L,L))
        S_new[:] = S[:]
        S_new[i][j] =  (-1) * (S_new[i][j])
      
        d_E = delta_E (S , L , 1 , i , j)
        
        if d_E<0:
            S = S_new
        else:
            w = min(1 , np.exp(-(beta*d_E)) )
            c = rn.random()
            if c<=w:
                S = S_new
                
    return S

def self_correlation(S , N):
    S = np.reshape(S , (1,N))
    C = np.zeros(N)
    C[0]=1
    sigma2 = np.var(S[0])
    for k in range(1,N):
        C[k] = ( np.mean(S[0][:-k]*S[0][k:]) - np.mean(S[0][:-k])*np.mean(S[0][k:]) )/sigma2
    return C

def length_of_correlation (C):
    i=0
    while i>=0 and i<L*L:
        if C[i]<=(np.exp(-1)):
            return (i-1)
        i+=1
    return 0


def E_array( M , N , L , q , beta , jump):
    
    E_array = np.zeros(int((N-q)/jump))
    for i in range (int((N-q)/jump)):
        E_array[i] = energy (M[i*jump +q] , L , 1)

    return E_array

def m_array(M , N , L , q , beta , jump):
    
    m_array = np.zeros(int((N-q)/jump))
    for i in range (int((N-q)/jump)):
        m_array[i] = magnetism (M[i*jump +q] , L )

    return m_array
    
    
def model_func(x,a):
     return np.exp(-x/a)    

#main code:
L=10
N=2000
q = 100 #we skip q steps of metropolice steps for equlibrium
jump = 20 #we jump 20 steps for vanishing the correlation
beta = np.linspace(0.2 , 0.7 , 25)


ksi = np.zeros(len(beta))


for i in range (len(beta)):
    M = montecarlo(L , N , beta[i])
    summation = 0
    for j in range (int((N-q)/jump)):
        C = self_correlation(M[(j*jump)+q], L*L)
        summation += length_of_correlation (C)
    ksi[i]= summation/(j+1)
    print(i)
plt.scatter(beta , ksi)
plt.plot(beta , ksi)
plt.xlabel("beta")
plt.ylabel("Ksi")
plt.title("Ksi in terms of beta")
plt.show()


#ki_L = 0

#for i in range (len(beta)):
    #if ksi[i]>ki_L:
        #ki_L = ksi[i]      
#print("ki_L = " , ki_L)

l = [10 , 20 , 30]
ksi_L = [0.7 , 1.1 , 1.5]
plt.scatter(np.log(l) , np.log(ksi_L) )
plt.xlabel("ln(L)")
plt.ylabel("ln(ksi_L)")
plt.title("ln(ksi_L) in terms of ln(L)")
plt.show()
a , b = np.polyfit(np.log(l) , np.log(ksi_L), 1)
print("v = " , a)

