import numpy as np
import random as rn
import matplotlib.pyplot as plt

def Creating_and_coloring_the_main_array (L , p): #This function creates the main array
    A = np.zeros((L,L))

    for i in range (L):
        A[i][0]=1
        A[i][L-1]=1000

    k=2
    for j in range (1,L):
        for i in range (L):
            c=rn.random()
            if c<= (float(p/100)):
                
                if A[i-1][j]==0  and A[i][j-1]==0 :
                   A[i][j]=k
                   k+=1
                elif A[i-1][j]!=0 and A[i][j-1]!=0:
                     e = max (A[i-1][j] , A[i][j-1])
                     A[i][j] = min (A[i-1][j] , A[i][j-1])
                     for m in range (1,L):
                         for n in range (L):
                             if A[n][m]==e:
                                 A[n][m]=A[i][j]
                elif A[i-1][j]==0:
                    A[i][j] = A[i][j-1]
                elif A[i][j-1]==0:
                    A[i][j] = A[i-1][j]

    for i in range (L):
        if A[i][L-1]==1000:
            A[i][L-1]=0
                

    return A #A is the main array which has been colored




def Recognizing_the_percolation (A , L):#This function recognizes the percolation
    for i in range (L):
        if A[i][L-1]==1:
            return 1
    return 0



#main code:
L = int(input("Enter the size of the lattice: "))
p = int(input("Enter the probability of turning on the lattice: ")) #p must be an integer

main_array = Creating_and_coloring_the_main_array (L , p)
R = Recognizing_the_percolation (main_array , L)



if R==0:
    print(R ,"\n", "Percolation has not occured")
else:
    print(R ,"\n", "Congratulations! Percolation has occured")


plt.imshow(main_array)
plt.show()
