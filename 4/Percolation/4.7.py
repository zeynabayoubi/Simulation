import numpy as np
import random as rn
import matplotlib.pyplot as plt


def creating_the_cluster (A , L , p): #This is a recursive function that creats the cluster
    for i in range (L):  #border conditions have been considered periodic
        for j in range (L):
            if A[i%L][j%L]==1:
                A[i%L][j%L]=11 # 11 means : Done 
                if A[i%L][(j+1)%L] == 0:
                    c = rn.random()
                    if c>=float(p) :
                        A[i%L][(j+1)%L] = 1 #1 means: Unlock
                        creating_the_cluster (A , L , p)
                    else:
                        A[i%L][(j+1)%L] = 2 #2 means: Block

                if A[(i+1)%L][j%L] == 0:
                    c = rn.random()
                    if c>=float(p) :
                        A[(i+1)%L][j%L] = 1 #1 means: Unlock
                        creating_the_cluster (A , L , p)
                    else:
                        A[(i+1)%L][j%L] = 2 #2 means: Block


                if A[i%L][(j-1)%L] == 0:
                    c = rn.random()
                    if c>=float(p) :
                        A[i%L][(j-1)%L] = 1 #1 means: Unlock
                        creating_the_cluster (A , L , p)
                    else:
                        A[i%L][(j-1)%L] = 2 #2 means: Block


                if A[(i-1)%L][j%L] == 0:
                    c = rn.random()
                    if c>=float(p) :
                        A[(i-1)%L][j%L] = 1 #1 means: Unlock
                        creating_the_cluster (A , L , p)
                    else:
                        A[(i-1)%L][j%L] = 2 #2 means: Block                  
                
    return A


def calcuting_S (A):
    S = 0
    for i in range (L):
        for j in range (L):
            if A[i][j]==11:
                S+=1
    return S

def length_of_correlation (A , L , S):
   
    center_of_mass_array = np.zeros((3 ,1))


    for i in range (L):
        for j in range (L):
            if A[i][j]==11 :
                center_of_mass_array[0] += i
                center_of_mass_array[1] += j
                center_of_mass_array[2] += 1
        
    center_of_mass_array[0] =  center_of_mass_array[0] / center_of_mass_array[2] #this contains the x component of center of mass 
    center_of_mass_array[1] =  center_of_mass_array[1] / center_of_mass_array[2] #this contains the y component of center of mass 
    # and the 3rd row of center_of_mass_array contains the number of members of this cluster
        


    d = np.zeros((2,1))

    for i in range (L):
        for j in range (L):
            if A[i][j]==11:
                d[0] += (center_of_mass_array[0] - i)**2
                d[1] += (center_of_mass_array[1] - j)**2

    length_of_correlation = 0
    length_of_correlation = d[0] + d[1]
    length_of_correlation = length_of_correlation / center_of_mass_array[2]
    length_of_correlation = (length_of_correlation)**(1/2)
            
    return length_of_correlation


def running(L, p):
    mean_S = 0
    mean_length_of_correlation = 0
    for i in range(100):
        A = np.zeros((L , L) , dtype=int)
        A [int(L/2) , int(L/2)] = 1
        D = creating_the_cluster (A , L , p)
        S = calcuting_S (D)
        mean_S += S
        mean_length_of_correlation += length_of_correlation(D , L , S)
    mean_length_of_correlation = mean_length_of_correlation / 100
    mean_S = mean_S / 100
    return mean_S , mean_length_of_correlation

#main code:

L = 10
p = [0.50 , 0.55 , 0.59]
A = np.zeros((L , L) , dtype=int)
A [int(L/2) , int(L/2)] = 1

S = np.zeros(len(p))
ksi = np.zeros(len(p))
ln_S = np.zeros(len(p))
ln_ksi = np.zeros(len(p))

for i in range (len(p)):
    S[i] , ksi[i] = running(L, p[i])
    ln_S[i] = np.log(S[i])
    ln_ksi[i] = np.log(ksi[i])
    
print ('S = ' , S)
print ('ksi = ' , ksi)
plt.scatter (ln_ksi , ln_S)
plt.plot(ln_ksi , ln_S)
plt.xlabel('ln(ksi)')
plt.ylabel('ln(S)')
plt.show()
m , b = np.polyfit(ln_ksi , ln_S , 1)
print ("m = ", m)

        
    
