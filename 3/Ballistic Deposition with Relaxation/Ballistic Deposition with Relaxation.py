import numpy as np
import random as rn
import matplotlib.pyplot as plt


def Creating_the_snowfall_pattern (L,m): #This function gives the main height array
    snowfall_pattern = np.zeros((m,L))
  
    for k in range (m):
        
        if k>0:
            snowfall_pattern[k][:]=snowfall_pattern[k-1][:]
                

            
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
        

    return snowfall_pattern



def Analysis (): #This function takes the snowfall pattern and gives the hbar_t and w_t
    C = Creating_the_snowfall_pattern (L,m)
    
    hbar_t = np.mean(C, axis = 1)
    w_t = np.std(C , axis=1)
    return hbar_t , w_t


def Run (N): #This function runs the code N times

    
    
    HBAR_T  = np.zeros(m)
    W_T  = np.zeros(m)

                    
    for i in range (N):
        A1 , A2 = Analysis()
        HBAR_T [:] += A1[:]
        W_T [:] += A2[:]

    HBAR_T  = HBAR_T/N
    W_T  = W_T/N


    return HBAR_T , W_T

#main code:

L= int(input("Enter the length: "))
m= int(input("Enter the number of the rows of the array: "))
N= int(input("Enter the iterations of running the code: "))

t = np.arange(1,m+1) 

R1 , R2 = Run(N)



for i in range (200, m):
    a , b = np.polyfit(np.log(t[i:]) , np.log(R2[i:]) , 1)
    if a<0.01:
        print(i)
        print("ln(saturation time): " ,np.log(t[i]))
        print("ln(saturation w): ",b)
        print("a: " , a)
        break
    
beta , bb=(np.polyfit(np.log(t[:100]) , np.log(R2[:100]),1))
print("beta= ",beta)



#plotting section:

    
#x=np.arange(1,201)
#C = Creating_the_snowfall_pattern (L,m)
#for i in range (20):
 #   plt.scatter(x , C[i])

#plt.legend(["Dataset 1", "Dataset 2", "Dataset 3", "Dataset 4","Dataset 5"])
#plt.xlabel('length')
#plt.ylabel('snowfall pattern')
#plt.show()

#plt.plot(t , R1)
#plt.xlabel('time')
#plt.ylabel('hbar')
#plt.show()

#plt.plot(t , R2)
#plt.xlabel('time')
#plt.ylabel('w(t)')
#plt.show()


#plt.scatter(np.log(t) , np.log(R2))
#plt.xlabel('ln(time)')
#plt.ylabel('ln(w(t)')
#plt.show()




