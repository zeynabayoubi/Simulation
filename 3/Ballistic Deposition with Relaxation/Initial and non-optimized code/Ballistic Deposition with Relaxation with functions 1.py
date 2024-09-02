import numpy as np
import random as rn
import matplotlib.pyplot as plt
import kneed
from kneed import KneeLocator


L= int(input("Enter the length: "))
m= int(input("Enter the number of the rows of the array: "))
N= int(input("Enter the iterations of running the code: "))


x= np.zeros(L)
for i in range (L):
    x[i]=i+1

    
t=np.zeros(m*5*L)
ln_t=np.zeros(m*5*L)
for i in range (m*5*L):
    t[i]=i+1
    ln_t[i]=np.log(t[i])


       
def Creating_the_snowfall_pattern (L,m): #m= number of the rows of the snowfall pattern
    snowfall_pattern = np.zeros((m,L))
    hbar_t = np.zeros(m*5*L)
    h2bar_t = np.zeros(m*5*L)

    for k in range (m):
        
        if k>0:
            i=0
            while i<L:
                snowfall_pattern[k][i]=snowfall_pattern[k-1][i]
                i+=1

            
        for i in range (5*L):
        
            c=rn.randint(0,L-1)
            if snowfall_pattern[k][c]<=snowfall_pattern[k][(c-1)%L] and snowfall_pattern[k][c]<=snowfall_pattern[k][(c+1)%L]:
                snowfall_pattern[k][c]+=1
            
            elif snowfall_pattern[k][(c-1)%L]<snowfall_pattern[k][(c+1)%L]:
                snowfall_pattern[k][(c-1)%L]+=1
            
            elif snowfall_pattern[k][(c-1)%L]>snowfall_pattern[k][(c+1)%L]:
                snowfall_pattern[k][(c+1)%L]+=1
            
            elif snowfall_pattern[k][(c-1)%L]==snowfall_pattern[k][(c+1)%L]:
                d=rn.randint(0,1)
                if d==0:
                    snowfall_pattern[k][(c-1)%L]+=1
                else:
                    snowfall_pattern[k][(c+1)%L]+=1

            
            
            hbar_t[i + (5*L)*k]=hbar_t[(i-1) + (5*L)*k]+1
            sum=0
            for j in range (L):
                sum+= snowfall_pattern[k][j]**2
            h2bar_t[i + (5*L)*k]=sum

    hbar_t=hbar_t/L
    h2bar_t=h2bar_t/L


    w_t=np.zeros(m*5*L)
    ln_w_t=np.zeros(m*5*L)
    for i in range (m*5*L):
        w_t[i]= (h2bar_t[i] - hbar_t[i]**2 )**(1/2)
        ln_w_t[i]=np.log(w_t[i])
        

    return snowfall_pattern , hbar_t , h2bar_t , w_t , ln_w_t





def Run (N,L,m):
    H_BAR_t=np.zeros(m*5*L)
    H2_BAR_t=np.zeros(m*5*L)
    W_t=np.zeros(m*5*L)
    LN_W_t=np.zeros(m*5*L)

    for j in range (N):
        C1 , C2 , C3 , C4 , C5 = Creating_the_snowfall_pattern (L,m)
        for i in range (m*5*L):
            H_BAR_t[i] += C2[i]
            H2_BAR_t[i] += C3[i]
            W_t[i] += C4[i]
            LN_W_t[i] +=C5[i]

    H_BAR_t = H_BAR_t/N
    H2_BAR_t = H2_BAR_t/N
    W_t = W_t/N
    LN_W_t = LN_W_t/N

    return H_BAR_t , H2_BAR_t , W_t , LN_W_t 



C1 , C2 , C3 , C4 , C5 = Creating_the_snowfall_pattern (L,m)
R1 , R2 , R3 , R4 = Run (N,L,m)


#saving ln(w(t)) in files:

np.save('Data for L=600 m=400 run=20' , R4 )




#plotting
#for i in range (m):
    #plt.plot(x , C1[i])

#plt.legend(["Dataset 1", "Dataset 2", "Dataset 3", "Dataset 4","Dataset 5"])
#plt.xlabel('length')
#plt.ylabel('snowfall pattern')
#plt.show()

#plt.plot(t , R1)
#plt.xlabel('time')
#plt.ylabel('hbar')
#plt.show()

#plt.plot(t , R3)
#plt.xlabel('time')
#plt.ylabel('w(t)')
#plt.show()


#plt.xscale('log')
#plt.yscale('log')
#plt.scatter(ln_t , R4 , s=0.1)
#plt.xlabel('ln(time)')
#plt.ylabel('ln(w(t)')
#plt.show()


#m,b=(np.polyfit(ln_t , R4 ,1))
#print("beta= ",m)



