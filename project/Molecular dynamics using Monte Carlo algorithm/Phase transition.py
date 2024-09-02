import numpy as np
import math as m
import random as rn
import matplotlib.pyplot as plt

def writeCoords(x,y):
        outfile.write("{0}\nComment\n".format(N))
        for i in range(N):
            outfile.write("{0:.5f}\t{1:.5f}\t{2:.5f}\n".format(x[i],y[i],0))


def place_atoms_left_side_regularly(N , L):
    positions = np.zeros((2 , N))
    half_size = m.ceil((N / 2) ** (1 / 2))
    grid_distance = L / 2 / half_size
    grid_sizes = np.array([1, half_size, *[2 * half_size for i in range(1)]])
    for axis in range(2):
        positions[axis] = np.tile(np.repeat(np.arange(grid_sizes[axis + 1]), np.prod(grid_sizes[:axis + 1])), np.prod(grid_sizes[axis:]))[:N]
    positions *= grid_distance
    positions += grid_distance / 2
    return positions[0] , positions[1]


def initial_velocities(N , v_max):
    Vx0 = np.random.uniform(-v_max , v_max , N) 
    Vy0 = np.random.uniform(-v_max , v_max , N) 
    Vx0 -= np.mean(Vx0)
    Vy0 -= np.mean(Vy0)
    return Vx0 , Vy0

def init(N , L , v_max):
    M = np.zeros((4,N))
    M[0] , M[1] = place_atoms_left_side_regularly(N , L)
    M[2] , M[3] = initial_velocities(N , v_max)
    return M

    
def E_Kinetic(Vx , Vy , N):
    kinetic_energy = 0
    for i in range (N):
        kinetic_energy += 0.5*(Vx[i]**2 + Vy[i]**2)
    return kinetic_energy


def E_Potential_and_pressure(X , Y , L , N , r_c , beta):
    a_x = np.zeros((N , N))
    a_y = np.zeros((N , N))
    potential_energy = np.zeros((N , N))
    pressure = np.zeros((N , N))
    for i in range(N):
        for j in range(i+1 ,N):   
            delta_x = X[i] - X[j]
            delta_y = Y[i] - Y[j]
            if delta_x >= L/2 :
                delta_x -= L
            if delta_x < -L/2 :
                delta_x += L
            if delta_y >= L/2 :
                delta_y -= L
            if delta_y < -L/2 :
                delta_y += L
            if abs(delta_x) <= r_c and abs(delta_y) <= r_c :
                r2 = delta_x**2 + delta_y**2
                if r2 <= r_c**2 :
                        r6 = r2 * r2 * r2
                        r12 = r6 * r6
                        c = ( (2/r12) - (1/r6) ) / r2
                        a_x[i][j] , a_x[j][i] = delta_x * c , -delta_x * c
                        a_y[i][j] , a_y[j][i] = delta_y * c , -delta_y * c
                        u = ( (1/r12) - (1/r6) )
                        potential_energy[i][j] = u
                        pressure[i][j] = a_x[i][j]*delta_x + a_y[i][j]*delta_y
    return 4 * np.sum(potential_energy) , ( N*(1/beta) + 0.5 * np.sum(pressure) )/(L*L)


def E_and_P(M , N , L , r_c , beta):
    E_K = E_Kinetic(M[2] , M[3] , N)
    E_P , P = E_Potential_and_pressure(M[0] , M[1] , L , N , r_c , beta)
    return E_K+E_P , E_K , E_P , P


def n_Right(X , L , N):
    n_r = 0
    for i in range (N):
        if X[i]>= (L/2):
            n_r +=1
    n_r = n_r/N
    return n_r


def metropolice(N , M , beta , Delta , L , r_c):
    for k in range(N):
        j = rn.randint(0,N-1)
        M_new = np.zeros((4,N))
        M_new[:] = M[:]
        s  = np.random.uniform(-1,1)
        M_new[0][j] =  (M_new[0][j] + Delta*s)%L
        M_new[1][j] =  (M_new[1][j] + Delta*s)%L
        d_E = E_Potential_and_pressure(M_new[0] , M_new[1] , L , N , r_c , beta)[0] - E_Potential_and_pressure(M[0] , M[1] , L , N , r_c , beta)[0]
        if d_E<0:
            M = M_new
        else:
            w = min(1 , np.exp(-(beta*d_E)) )
            c = rn.random()
            if c<=w:
                M = M_new
    return M


def montecarlo(n , N , beta , Delta , L , r_c , M):
    NVT = []
    NVT.append(M)
    for i in range (n):
        M = metropolice(N , M , beta , Delta , L , r_c)
        #writeCoords(M[0] , M[1])
        NVT.append(M)
        print(i)
    return NVT

def auto_correlation(E , m):
    C = np.zeros(m)
    C[0]=1
    w = True
    tau = 0
    sigma2 = np.var(E)
    if sigma2 == 0:
        return 0
    for k in range (1 , m):
        C[k] = ( np.mean(E[:-k]*E[k:]) - np.mean(E[:-k])*np.mean(E[k:]) )/sigma2
        if C[k] <= np.exp(-1) and w:
                tau  = k
                w = False
        return C , tau

def temprature(E_K , N):
    return E_K/N
    

#main code:
L = 30
N = 100
r_c = 2.5
Delta = 0.7
n = 500
v_max = np.linspace(0.5 , 2 , 7)
v_max = v_max[::-1]
quantities = np.zeros((5 , len(v_max)*int(n/10)))
mean_quantities = np.zeros((5,len(v_max)))
M = init(N , L , v_max[0])
#outfile = open('outfile.xyz' , 'w')
#writeCoords(M[0] , M[1])
for k in range (len(v_max)):
    print("v_max =" , v_max[k])
    beta = (E_Kinetic(M[2] , M[3] , N)/N)**(-1)
    print("beta =" , beta)
    NVT = montecarlo(n , N , beta , Delta , L , r_c , M)
    if k<(len(v_max)-1):
        M = np.zeros((4,N))
        M[0] , M[1] = NVT[len(NVT)-1][0] , NVT[len(NVT)-1][1]
        M[2] , M[3] = initial_velocities(N , v_max[k+1])
    E_and_P_array = np.zeros((5 , int(len(NVT)/10)))
    
    for i in range (int(len(NVT)/10)):
        E_and_P_array[0][i] = E_and_P(NVT[10*i] , N , L , r_c , beta)[0]
        E_and_P_array[1][i] = E_and_P(NVT[10*i] , N , L , r_c , beta)[1]
        E_and_P_array[2][i] = E_and_P(NVT[10*i] , N , L , r_c , beta)[2]
        E_and_P_array[3][i] = E_and_P(NVT[10*i] , N , L , r_c , beta)[3]
    for j in range (4):
        mean_quantities[j][k] = np.mean(E_and_P_array[j][20:])
    mean_quantities[4][k] = (1/beta)
    E_and_P_array[4][:] = (1/beta)
    for j in range (5):
        for i in range (int(len(NVT)/10)):
            quantities[j][i + k*int(n/10)] = E_and_P_array[j][i]
#outfile.close()        
print("list of total energy =" , mean_quantities[0] , "\n") 
print("list of kinetic energy =" , mean_quantities[1] , "\n")        
print("list of kpotential energy =" , mean_quantities[2] , "\n")
print("list of pressure =" , mean_quantities[3] , "\n")
print("list of temperature =" , mean_quantities[4] , "\n") 
    
i = np.arange(0 ,len(v_max)*int(n/10))
plt.plot(i , quantities[0])
plt.plot(i , quantities[1])
plt.plot(i , quantities[2])
plt.title("Energy Diagram")
plt.xlabel("monte carlo steps")
plt.ylabel("Energy[*epsilon]")
plt.legend(["total energy" , "kinetic energy" , "potential energy"])
plt.show()
plt.plot(i , quantities[4])
plt.title("Temprature")
plt.xlabel("monte carlo steps")
plt.ylabel("Temprature[*epsilon/K_B]")
plt.show()
plt.plot(i , quantities[3])
plt.title("pressure")
plt.xlabel("monte carlo steps")
plt.ylabel("pressure[*epsilon/sigma^2]")
plt.show()


m , b = np.polyfit(mean_quantities[0] , mean_quantities[4] , 1)
x = np.linspace(mean_quantities[0][0], mean_quantities[0][len(v_max)-1] , 7)
y = m*x + b
plt.plot(x,y)
plt.scatter(mean_quantities[0] , mean_quantities[4])
#plt.plot (Energy , temperature)
plt.title("Temperature in terms of energy")
plt.xlabel("Energy(*epsilon)")
plt.ylabel("Temperature(* epsilon/K_B )")
plt.legend(["fitted line"  , "samples"])
plt.show()
print("for Temperature in terms of energy diagram: \n" , "m =" , m , "\n" , "b =" , b , "\n\n")


m , b = np.polyfit(mean_quantities[0] , mean_quantities[3] , 1)
x = np.linspace(mean_quantities[0][0] , mean_quantities[0][len(v_max)-1] , 7)
y = m*x + b
plt.plot(x,y)
plt.scatter(mean_quantities[0], mean_quantities[3])
#plt.plot (Energy , pressure)
plt.title("Pressure in terms of energy")
plt.xlabel("Energy(*epsilon)")
plt.ylabel("Pressure(*  epsilon/(sigma)^2  )")
plt.legend(["fitted line"  , "samples"])
plt.show()
print("for pressure in terms of energy diagram: \n" , "m =" , m , "\n" , "b =" , b , "\n\n")


m , b = np.polyfit(mean_quantities[4] , mean_quantities[3] , 1)
x = np.linspace (mean_quantities[4][0] , mean_quantities[4][len(v_max)-1] , 7)
y = m*x + b
plt.plot(x,y)
plt.scatter (mean_quantities[4] , mean_quantities[3])
#plt.plot (temperature, pressure)
plt.title("pressure in terms of temperature in different energies")
plt.xlabel("Temperature(* epsilon/K_B )")
plt.ylabel("Pressure(*  epsilon/(sigma)^2  )")
plt.show()
print("for pressure in terms of temperature in different energies diagram: \n" , "m =" , m , "\n" , "b =" , b , "\n\n")
