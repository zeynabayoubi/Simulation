import numpy as np
import random as rn
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


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


def length_of_correlation (L , p):
    A, S, map_array = Hoshen_Keoplman(L, p)
    r = Recognizing_the_percolation(A, L, map_array)
    
    if r == 1:
        S[1] = 0
    S[0] = 0
        
    max_label = np.argpartition(S, -2)[-2] ## find label of second biggest cluster
    if S[max_label] == 0:
        return 0
    
    max_cluster_coordinates = []
    for i in range(L):
        for j in range(L):
            if A[i, j] == max_label:
                max_cluster_coordinates.append(i + j * 1j)
            
    return np.std(max_cluster_coordinates)


def running(L, p):
    mean_length_of_correlation = 0
    for i in range(100):
        mean_length_of_correlation += length_of_correlation(L, p)
    mean_length_of_correlation = mean_length_of_correlation / 100
    return mean_length_of_correlation


#main code:
#L = int ( input ( "Enter the length: " ) )

L = np.array([10, 20, 40, 80, 160])
P = np.array([0,0.1,0.2,0.3,0.4,0.45,0.50,0.51,0.55,0.58,0.59,0.6,0.61,0.62,0.65,0.67,0.7,0.8,0.9,1])
ksi_array = np.zeros(len(P))
ksi_max = np.zeros(len(L))
p_c_L = np.zeros(len(L))

for k in range (len(L)):
    for i in range(len(P)):
        print(f"\rL: {L[k]} \t P: {P[i]}", end="")
        ksi_array[i] = running(L[k], P[i])
        if (ksi_array[i] > ksi_max[k]):
            ksi_max[k] = ksi_array[i]
            p_c_L[k] = P[i]
            
    plt.scatter(P, ksi_array)
    plt.plot(P, ksi_array)

plt.legend([f"L={L_i}" for L_i in L])
plt.xlabel("the probability of turning on the lattice")
plt.ylabel("length of correlation")
plt.show()

plt.scatter(L , ksi_max)
plt.plot(L , ksi_max)
plt.xlabel("length of the lattice")
plt.ylabel("maximum length of correlation")
plt.show()

print("\n\n")
print ("maximum length of correlation = " , ksi_max , '\n')
print ("p_c(L) = " , p_c_L , '\n')

plt.scatter(L , p_c_L)
plt.plot(L , p_c_L)
plt.xlabel("length of the lattice")
plt.ylabel("p_c_L")
plt.show()




def p_infinity_model(p, p_inf, A, v): #This section of code has been written from Sina's githob
    return (A * np.abs(p - p_inf)) ** (-v)
fit_para, fit_error = curve_fit(p_infinity_model, p_c_L, L, p0=(.6, 1, 1.4))
fit_error = np.diag(fit_error)
p_c_inf = fit_para[0]
print('p_c(∞) = ' + str(fit_para[0]) + ' ± ' + str(fit_error[0]))


ln_pcinf_pcl = np.zeros(len(L))
ln_L = np.zeros(len(L))

for i in range (len(L)):
    ln_L[i] = np.log(L[i])
    ln_pcinf_pcl[i] =  np.log( p_c_inf - p_c_L[i] )

plt.scatter(ln_L , ln_pcinf_pcl)
plt.plot(ln_L , ln_pcinf_pcl)
plt.xlabel("ln(length of the lattice)")
plt.ylabel("ln (p_c(inf) - p_c(L) )")
plt.show()

m  , b = np.polyfit (ln_L , ln_pcinf_pcl , 1)
print("v = " , (0 - m ))

    

    
    
