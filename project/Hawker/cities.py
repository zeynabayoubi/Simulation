import numpy as np
import random as rn
import matplotlib.pyplot as plt

def cities_coordinates(n):
    x_cities = np.random.uniform(0,10,n)
    y_cities = np.random.uniform(0,10,n)
    return x_cities , y_cities

def total_distance(order_of_cities_array , x_cities , y_cities , n):
    distance = 0
    for i in range (0 , n-1):
        d = 0
        d += ( x_cities[int(order_of_cities_array[i])] - x_cities[int(order_of_cities_array[i+1])] )**2
        d += ( y_cities[int(order_of_cities_array[i])] - y_cities[int(order_of_cities_array[i+1])] )**2
        d = d**(1/2)
        distance += d
    return distance

def initial_population(n , m):
    pop = np.zeros((m , n))
    for i in range (m):
        pop[i] = rn.sample(range(n) , n)
    return pop

def fitness(population , m , x_cities , y_cities , n):
    f = np.zeros(m)
    for i in range (m):
        f[i] = total_distance(population[i] , x_cities , y_cities , n)
    return f
   
def sort (population , fit , n , m):
    total_array = np.zeros((m , n+1))
    for i in range (m):
        total_array[i][0] = fit[i]
        for j in range (1 , n+1):
            total_array[i][j] = population[i][j-1]
    total_array = list(total_array)
    total_array.sort(key = lambda tup: tup[0])
    total_array = np.array(total_array)
    for i in range (m):
        fit[i] = total_array[i][0] 
        for j in range (1 , n+1):
            population[i][j-1] = total_array[i][j]
    return population , fit

def next_generation(sorted_population , n , m , posibilities):
    new_pop = np.zeros((m , n))
    new_pop[:][:] = 1000
    new_pop[0] , new_pop[1] = sorted_population[0] , sorted_population[1]
    listt = np.arange(0,m)
    for i in range (1,int((m-2)/2)+1):
        c1 = np.random.choice(listt,p=posibilities)
        c2 = np.random.choice(listt,p=posibilities)
        new_pop[2*i][:int(n/2)] = sorted_population[c1][:int(n/2)]
        new_pop[2*i+1][:int(n/2)] = sorted_population[c2][:int(n/2)]
        for j in range (int(n/2) , n):
            for k in range (n):
                for s in range (j):
                    if sorted_population[c2][k] == new_pop[2*i][s]:
                        break
                    if s == (j-1) :
                        new_pop[2*i][j] = sorted_population[c2][k]
                if new_pop[2*i][j] == sorted_population[c2][k] :
                    break
        for j in range (int(n/2) , n):
            for k in range (n):
                for s in range (j):
                    if sorted_population[c1][k] == new_pop[2*i+1][s]:
                        break
                    if s == (j-1) :
                        new_pop[2*i+1][j] = sorted_population[c1][k]
                if new_pop[2*i+1][j] == sorted_population[c1][k]:
                    break
        c = rn.random()
        if c<0.08:
            d1 = rn.randint(0,n-1)
            d2 = rn.randint(0,n-1)
            d = new_pop[i][d1]
            new_pop[i][d1] = new_pop[i][d2]
            new_pop[i][d2] = d
            
    return new_pop

n = 15 #number of the cities
m = 100 #number of each population

posibilities = (1/(m*(m+1)/2))*np.arange(1 , m+1)
posibilities = posibilities[::-1]

x_cities , y_cities = cities_coordinates(n)
print("x_cities = ","\n",x_cities)
print("y_cities = ","\n",y_cities)
P0 = initial_population(n , m)
fit_p0 = fitness(P0 , m , x_cities , y_cities , n)
sorted_pop , sorted_fit = sort (P0 , fit_p0 , n , m)
print("initial distance =" , sorted_fit[0])
run = 1000
best_distance = np.zeros(run)

for i in range (run):
    new_population = next_generation(sorted_pop , n , m , posibilities)
    fit = fitness(new_population , m , x_cities , y_cities , n)
    sorted_pop , sorted_fit = sort (new_population , fit , n , m)
    best_distance[i] = sorted_fit[0]
    print(i)
print("best distance =" , best_distance[run-1])
print("best order of cities =", "\n" , sorted_pop[0])
number_of_generations = np.arange(1,run+1)
plt.xlabel("number of generation")
plt.ylabel("best distance")
plt.title("Population of each generation is {a} and the number of generations is {b} ".format(a = m , b = run))
plt.plot(number_of_generations , best_distance)
plt.show()


