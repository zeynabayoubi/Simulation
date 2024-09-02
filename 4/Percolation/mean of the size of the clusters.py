import numpy as np
import random as rn
import matplotlib.pyplot as plt


def Hoshen_Keoplman(L, p):  # This function creats the percolation array with Hoshen_Keoplman algorithm

    A = np.zeros((L, L+1), dtype=int)  # This is the main array of percolation ## Sina
    S = np.zeros(L * L)  # This is an array that contains the size of the clusters
    

    map_array = np.arange(0, L * L)  # This is an array that contains the map of pointers

    for i in range(L):
        A[i][0] = 1

    k = 2
    
    for j in range(1, L+1):
        for i in range(L):
            c = rn.random()

            if c <= float(p):

                if A[i - 1][j] == 0 and A[i][j - 1] == 0:

                    A[i][j] = k
                    S[k] += 1
                    k += 1

                elif A[i - 1][j] == 0:

                    a = proc(int(A[i, j - 1]), map_array) 
                    A[i][j] = a
                    S[a] += 1

                elif A[i][j - 1] == 0:

                    a = proc(int(A[i - 1, j]), map_array) 
                    A[i][j] = a
                    S[a] += 1

                elif A[i - 1][j] != 0 and A[i][j - 1] != 0:

                    e = proc(int(A[i - 1][j]), map_array) 
                    a = proc(int(A[i][j - 1]), map_array)
                    d = min(a, e)
                    f = max(a, e)

                    A[i][j] = d

                    if a == e:
                        S[a] += 1
                    else:
                        b1 = a
                        b2 = e
                        b3 = d
                        b4 = f

                        S[b3] = S[b1] + S[b2] + 1

                        S[b4] = 0
                        map_array[b4] = b3


    B = np.zeros((L, L), dtype=int)
    for i in range(L): 
        for j in range(1,L+1):
            A[i, j] = proc(A[i, j], map_array)
            B[i, j-1] = A[i, j]
            
    return B, S, map_array


def proc(k, w):  # This ia a recursive function that can write the map array
    if w[k] == k:
        return w[k]
    else:
       w[k] = proc(w[k], w) 
       return w[k]


def Recognizing_the_percolation(A, L, map_array):  # This function recognizes the percolation
    for i in range(L):
        a = int(A[i][L - 1])
        b = proc(a, map_array)
        if b == 1:
            return 1
    return 0


def calcuting_the_mean_of_size_of_clusters(L, p):  # This function calcutes the mean of size of clusters
    ksi = 0
    main_array, S, map_array = Hoshen_Keoplman(L, p)
    r = Recognizing_the_percolation(main_array, L, map_array)

    if r == 0:
        SUM = 0
        s = 0

        for i in range(2,L * L):
            if S[i] != 0:
                SUM += S[i]
                s += 1
        if s == 0:
            ksi = 0
        else:
            ksi = SUM / s

    else:
        SUM = 0
        s = 0

        for i in range(2, L * L):
            if S[i] != 0:

                SUM += S[i]
                s += 1
        if s == 0:
            ksi = 0
        else:
            ksi = SUM / s
    return ksi


def running(L, p):
    mean_ksi = 0
    for i in range(100):
        mean_ksi += calcuting_the_mean_of_size_of_clusters(L, p)
    mean_ksi = mean_ksi / 100
    return mean_ksi


# main code:

#L = int ( input ( "Enter the length: " ) )
P = np.linspace(0, 1, 20)
L = [10, 20, 40, 80, 160]
#P = [0,0.1,0.2,0.3,0.4,0.45,0.50,0.51,0.55,0.58,0.59,0.6,0.61,0.62,0.65,0.67,0.7,0.8,0.9,1]
ksi_array = np.zeros(len(P))

for k in range (len(L)):
    for i in range(len(P)):
        print(f"\rL: {L[k]} \t P: {P[i]}", end="")
        ksi_array[i] = running(L[k], P[i])
    plt.scatter(P, ksi_array)
    plt.plot(P, ksi_array)

plt.legend([f"L={L_i}" for L_i in L])
plt.xlabel("the probability of turning on the lattice")
plt.ylabel("mean of size of clusters")
plt.show()
