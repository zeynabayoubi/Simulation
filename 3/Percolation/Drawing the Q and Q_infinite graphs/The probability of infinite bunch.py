import numpy as np
import random as rn
import matplotlib.pyplot as plt

def Creating_and_coloring_the_main_array (L , p): #This function creates the main array and colors it
    A = np.zeros((L,L))

    for i in range (L):
        A[i][0]=1
        A[i][L-1]=1000

    k=2
    for j in range (1,L):
        for i in range (L):
            c=rn.random()
            if c<= (p):
                
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


def The_probability_of_infinite_bunch(L): #This function gives Q
    P = np.arange (0 , 1 , 0.05)
    Q = np.zeros(20)

    for i in range (20):
        sum = 0
        for j in range (100):
            main_array = Creating_and_coloring_the_main_array (L , P[i])
            R = Recognizing_the_percolation (main_array , L)
            sum+=R
        Q[i]=float(sum/100)
    return Q


def The_probability_of_maching_the_infinite_bunch(L): #This function gives the Q(infinite)
    P = np.arange (0 , 1 , 0.05)
    Q_inf = np.zeros(20)

    for i in range (20):
        sum = 0
        for j in range (100):
            main_array = Creating_and_coloring_the_main_array (L , P[i])
            R = Recognizing_the_percolation (main_array , L)
            if R==1:
                c1 = rn.randint(0,L-1)
                c2 = rn.randint(0,L-1)
                if (main_array[c1][c2])==1:
                    sum+=R
        Q_inf[i]=float(sum/100)
    return Q_inf


            
#main code:

L1=10
L2=20
L3=30

P = np.arange (0 , 1 , 0.05)
Q1 = The_probability_of_infinite_bunch(L1)
Q2 = The_probability_of_infinite_bunch(L2)
Q3 = The_probability_of_infinite_bunch(L3)

plt.plot(P , Q1)
plt.plot(P , Q2)
plt.plot(P , Q3)

plt.xlabel('The probability of turning on the lattice')
plt.ylabel('The_probability_of_infinite_bunch')
plt.legend(["L=10", "L=20", "L=30"])
plt.show()



Q1_inf = The_probability_of_maching_the_infinite_bunch(L1)
Q2_inf = The_probability_of_maching_the_infinite_bunch(L2)
Q3_inf = The_probability_of_maching_the_infinite_bunch(L3)

plt.plot(P , Q1_inf)
plt.plot(P , Q2_inf)
plt.plot(P , Q3_inf)

plt.xlabel('The probability of turning on the lattice')
plt.ylabel('The probability of maching the infinite bunch')
plt.legend(["L=10", "L=20", "L=30"])
plt.show()




