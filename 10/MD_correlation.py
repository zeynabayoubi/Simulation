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

def initial_velocities(L , N , v_max):
  
    Vx0 = np.random.uniform(-v_max , v_max , N) 
    Vy0 = np.random.uniform(-v_max , v_max , N) 
    
    Vx0 -= np.mean(Vx0)
    Vy0 -= np.mean(Vy0)

    return Vx0 , Vy0

def accel(X , Y , L , N , r_c):
        
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

    return 24 * np.sum(a_x , axis = 1) , 24 * np.sum(a_y , axis = 1) , 4 * np.sum(potential_energy) , 0.5 * np.sum(pressure)


def MD(X , Y , Vx , Vy , a_x , a_y , L , N , h , r_c):

    X[:] = (X[:] + Vx[:]*h + 0.5*a_x[:]*h*h) % L
    Y[:] = (Y[:] + Vy[:]*h + 0.5*a_y[:]*h*h) % L
    
    Vx[:] = Vx[:] + 0.5*a_x[:]*h
    Vy[:] = Vy[:] + 0.5*a_y[:]*h
        
    a_x , a_y  , U , P = accel(X , Y , L , N , r_c)

    Vx[:] = Vx[:] + 0.5*a_x[:]*h
    Vy[:] = Vy[:]+ 0.5*a_y[:]*h
    
    Vx -= np.mean(Vx)
    Vy -= np.mean(Vy)
    
    return X , Y , Vx , Vy , a_x , a_y , U , P


def E_Kinetic(Vx , Vy , N):
        
        kinetic_energy = 0
        for i in range (N):
                kinetic_energy += 0.5*(Vx[i]**2 + Vy[i]**2)
   
        return kinetic_energy 


def n_Right(X , L , N):
    
    n_r = 0
    for i in range (N):
        if X[i]>= (L/2):
            n_r +=1
    n_r = n_r/N

    return n_r

def auto_correlation(V , M):
        
        C = [1]
        w = True
        tau = 0
        V = np.array(V)
        sigma2 = np.var(V)

        if sigma2 == 0:
                return 0
        
        for k in range (1 , M):
                a = np.mean(V[:-k]*V[k:]) / sigma2
                C.append(np.mean(a))
                if a <= np.exp(-1) and w:
                        tau  = k
                        w = False
        return C , tau
                   

L = 30
N = 100
T = 10
h = 0.001
r_c = 2.5
v_max = 1.5
n_s = 10

X , Y = place_atoms_left_side_regularly(N , L)
Vx , Vy = initial_velocities(L , N , v_max)

outfile = open('outfile.xyz' , 'w')
writeCoords(X , Y)

a_x , a_y  , U , P = accel(X , Y , L , N , r_c)

t = np.arange(0,T,h)

Kinetic_Energy = []
Potential_Energy = []
Temperature = []
Pressure = []
n_R = []
V = []

Correlation = np.zeros( int(len(t)/n_s) )
for i in range (len(t)):
    X , Y , Vx , Vy , a_x , a_y , U , P = MD(X , Y , Vx , Vy , a_x , a_y , L , N , h , r_c)
    if i%n_s == 0:
        m = np.zeros((2,N))
        m[0][:] = Vx[:]
        m[1][:] = Vy[:]
        V.append(m)
        K = E_Kinetic(Vx , Vy , N)
        Kinetic_Energy.append(K)
        Potential_Energy.append(U)
        Temperature.append(K/N)
        Pressure.append( (K + P) / (L*L) )
        n_R.append(n_Right(X , L , N))
        print(i) 
        writeCoords(X , Y)
outfile.close()


Kinetic_Energy = np.array(Kinetic_Energy)
Potential_Energy = np.array(Potential_Energy  )
Total_Energy = Kinetic_Energy + Potential_Energy


t = np.linspace(0,T,len(Total_Energy))
Cv , tau = auto_correlation(V , len(Total_Energy))

print ("tau = " , tau*n_s*h)

plt.scatter(t , Cv)
plt.plot(t , Cv)
plt.xlim(0,8)
plt.title("Auto correlation of velocities")
plt.xlabel("time (*tau)")
plt.ylabel("correlation")
plt.show()







