import numpy as np
import random as rn
import matplotlib.pyplot as plt



def Creating_the_snowfall_pattern (L,m): #This function gives the main height array
    snowfall_pattern = np.full((m,L),-1000)
    snowfall_pattern[0][int(L/2)]=0
    
    for k in range (m):
        
        if k>0:
                snowfall_pattern[k][:]=snowfall_pattern[k-1][:]

            
        for i in range (5*L):
        
            c=rn.randint(0,L-1)
            snowfall_pattern[k][c]=max(snowfall_pattern[k][(c-1)%L] , snowfall_pattern[k][c]+1, snowfall_pattern[k][(c+1)%L])

    return snowfall_pattern




#main code:

L= 500
m= 40 #number of the rows or the main array

C = Creating_the_snowfall_pattern (L,m)
t = np.arange(1,m+1) 
wide = np.zeros(m)

for i in range (m): #This loop fills the wide array
    for j in range (L):
        if C[i][j] >= 0:
            for k in range(j , L):
                if C[i][k]<0:
                    wide[i] = k-j
                    break
            break
        
    


#plotting section:

    
x=np.arange(1,L+1)

for i in range (m):
    plt.scatter(x , C[i])

plt.legend(["Dataset 1", "Dataset 2", "Dataset 3", "Dataset 4","Dataset 5"])
plt.xlabel('length')
plt.ylabel('snowfall pattern')
plt.show()


plt.scatter(t , wide)
plt.xlabel('time')
plt.ylabel('wide')
plt.show()

m , b = np.polyfit(t, wide ,1)
print(m)

plt.scatter(np.log(t) , np.log(wide))
plt.xlabel('ln(time)')
plt.ylabel('ln(wide)')
plt.show()

m , b = np.polyfit(np.log(t), np.log(wide) ,1)
print(m)

