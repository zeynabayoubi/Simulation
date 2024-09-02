import numpy as np
import random as rn
import matplotlib.pyplot as plt

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

def self_correlation(E , N):
   
    C = np.zeros(N)
    C[0]=1
    sigma2 = np.var(E)
    for k in range(1,N):
        C[k] = ( np.mean(E[:-k]*E[k:]) - np.mean(E[:-k])*np.mean(E[k:]) )/sigma2
    return C

def length_of_correlation (C):
    i=0
    while i>=0 :
        if C[i]<(1/2.72):
            return i
        i+=1

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
    
    
    

#main code:
L=10
N=2000
q = 100 #we skip q steps of metropolice steps for equlibrium
jump = 20 #we jump 20 steps for vanishing the correlation
beta = np.linspace(0.2 , 0.7 , 25)

Cv_beta = np.zeros(len(beta))
ki_beta = np.zeros(len(beta))
abs_mean_m = np.zeros(len(beta))
m = np.zeros(N-q)
E = np.zeros(N-q)
ksi = np.zeros(len(beta))
correlation = np.zeros(N-q)

for i in range (len(beta)):
    M = montecarlo(L , N , beta[i])
    Cv_beta[i] = Cv (E_array(M , N , L , q , beta[i] , jump), L , beta[i])
    ki_beta[i] = Ki (m_array(M , N , L , q , beta[i] , jump), L , beta[i])
    for j in range (N-q):
        m[j] = magnetism (M[j+q] , L)
        E[j] = energy (M[j+q] , L , 1)
    correlation[:] = self_correlation(E , N-q)[:]
    abs_mean_m[i] = abs(np.mean(m))
    ksi[i] = length_of_correlation (correlation)
    print(i)

plt.scatter(beta , Cv_beta)
plt.plot(beta , Cv_beta)
plt.xlabel("beta")
plt.ylabel("Cv")
plt.title("Cv in terms of beta")
plt.show()
    
plt.scatter(beta , ki_beta)
plt.plot(beta , ki_beta)
plt.xlabel("beta")
plt.ylabel("Ki")
plt.title("Ki in terms of beta")
plt.show()


plt.scatter(beta , abs_mean_m)
plt.plot(beta , abs_mean_m)
plt.xlabel("beta")
plt.ylabel("abs_mean_m")
plt.title("abs_mean_m in terms of beta")
plt.show()

plt.scatter(beta , ksi)
plt.xlabel("beta")
plt.ylabel("Ksi")
plt.title("Ksi in terms of beta")
plt.show()

#Cv_L = 0
l = [10 , 20 , 30]

#for i in range (len(beta)):
    #if Cv_beta[i]>Cv_L:
        #Cv_L = Cv_beta[i]        
#print("Cv_L = " , Cv_L)

Cv_L = [0.40 , 0.45 , 0.60]
plt.scatter(np.log(l) , np.log(Cv_L) )
plt.xlabel("ln(L)")
plt.ylabel("ln(Cv_L)")
plt.title("ln(Cv_L) in terms of ln(L)")
plt.show()
a , b = np.polyfit(np.log(l) , np.log(Cv_L), 1)
print("c0 = " , a)


#ki_L = 0

#for i in range (len(beta)):
    #if ki_beta[i]>ki_L:
        #ki_L = ki_beta[i]      
#print("ki_L = " , ki_L)


ki_L = [22.43, 37.08, 69.01]
plt.scatter(np.log(l) , np.log(ki_L) )
plt.xlabel("ln(L)")
plt.ylabel("ln(ki_L)")
plt.title("ln(ki_L) in terms of ln(L)")
plt.show()
a , b = np.polyfit(np.log(l) , np.log(ki_L), 1)
print("gama = " , a)


plt.scatter(np.log(l) , np.log(m_L) )
plt.xlabel("ln(L)")
plt.ylabel("ln(m_L)")
plt.title("ln(m_L) in terms of ln(L)")
plt.show()
a , b = np.polyfit(np.log(l) , np.log(m_L) , 1)
print("beta = " , -a)



