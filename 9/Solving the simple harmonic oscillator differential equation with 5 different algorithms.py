import numpy as np
import matplotlib.pyplot as plt

# Analytic solution:
def Analytic_solution():
    
    t = np.arange(0 , 60 , 0.1)
    
    x_t = np.zeros(len(t))
    v_t = np.zeros(len(t))

    x_t[:] = np.cos(t[:])
    v_t[:] = -np.sin(t[:])
    
    return x_t , v_t 


def Euler():

    t = np.arange(0 , 60 , 0.1)
    
    x_t = np.zeros(len(t))
    v_t = np.zeros(len(t))
    x_t[0] = 1

    h = 0.01

    x=1
    v=0
    a = -x

    for i in range(60*int(1/h)):
        
        x = x + v*h
        v = v + a*h
        a = -x

        if (i+1)%10 == 0:
            if int((i+1)/10) < len(t):
                x_t[int((i+1)/10)] = x
                v_t[int((i+1)/10)] = v

    return x_t , v_t


def Euler_Cromer():

    t = np.arange(0 , 60 , 0.1)
    
    x_t = np.zeros(len(t))
    v_t = np.zeros(len(t))
    x_t[0] = 1

    h = 0.01

    x=1
    v=0
    a = -x

    for i in range(60*int(1/h)):
        
        v = v + a*h
        x = x + v*h
        a = -x

        if (i+1)%10 == 0:
            if int((i+1)/10) < len(t):
                x_t[int((i+1)/10)] = x
                v_t[int((i+1)/10)] = v

    return x_t , v_t


def Verlet():

    t = np.arange(0 , 60 , 0.1)
    
    x_t = np.zeros(len(t))
    v_t = np.zeros(len(t))
    x_t[0] = 1
    x_t[1] = 1

    h = 0.01

    x0=1
    v=0
    x1 = x0 + v*h #Euler
    a = -x1

    for i in range(60*int(1/h)):
        
        x2 = 2*x1 - x0 + h*h*a
        v = (x2-x0)/(2*h)
        x0 = x1
        x1 = x2
        a = -x1

        if (i+1)%10 == 0:
            if int((i+1)/10) < len(t):
                x_t[int((i+1)/10)] = x2
                v_t[int((i+1)/10)] = v

    return x_t , v_t


def Velocity_Verlet():

    t = np.arange(0 , 60 , 0.1)
    
    x_t = np.zeros(len(t))
    v_t = np.zeros(len(t))
    x_t[0] = 1

    h = 0.01

    x=1
    v=0
    a = -x

    for i in range(60*int(1/h)):
        
        x = x + v*h + 0.5*h*h*a
        v = v + 0.5*a*h
        a = -x
        v = v + 0.5*a*h

        if (i+1)%10 == 0:
            if int((i+1)/10) < len(t):
                x_t[int((i+1)/10)] = x
                v_t[int((i+1)/10)] = v

    return x_t , v_t


def Beeman():

    t = np.arange(0 , 60 , 0.1)
    
    x_t = np.zeros(len(t))
    v_t = np.zeros(len(t))
    x_t[0] = 1
    x_t[1] = 1

    h = 0.01

    x0=1
    v=0
    a0 = -x0
    x = x0 + v*h #Euler
    v = v + a0*h #Euler
    a1 = -x

    for i in range(60*int(1/h)):
        
        x = x + v*h + (1/6)*h*h*(4*a1 - a0)
        v = v + (1/6)*h*(5*a1 - a0)
        a0 = a1
        a1 = -x
        v = v + (2/6)*h*a1

        if (i+1)%10 == 0:
            if int((i+1)/10) < len(t):
                x_t[int((i+1)/10)] = x
                v_t[int((i+1)/10)] = v

    return x_t , v_t



t = np.arange(0 , 60 , 0.1)
    
x_t = np.zeros((6 , len(t)))
v_t = np.zeros((6 , len(t)))

x_t[0][:] , v_t[0][:] = Analytic_solution()
x_t[1][:] , v_t[1][:] = Euler()
x_t[2][:] , v_t[2][:] = Euler_Cromer()
x_t[3][:] , v_t[3][:] = Velocity_Verlet()
x_t[4][:] , v_t[4][:] = Beeman()
x_t[5][:] , v_t[5][:] = Verlet()

plt.plot(t , x_t[0])
plt.plot(t , x_t[1])
plt.plot(t , x_t[2])
plt.plot(t , x_t[3])
plt.plot(t , x_t[4])
plt.plot(t , x_t[5])

plt.xlabel("t")
plt.ylabel("X(t)")
plt.legend(["Analytic solution" , "Euler" , "Euler-Cromer" , "Velocity-Verlet" , "Beeman" , "Verlet"])
plt.show()

#Phase Diagram

plt.plot(x_t[0] , v_t[0])
plt.xlabel("X(t)")
plt.ylabel("V(t)")
plt.title("Analytic solution")
plt.show()

plt.plot(x_t[1] , v_t[1])
plt.xlabel("X(t)")
plt.ylabel("V(t)")
plt.title("Euler")
plt.show()

plt.plot(x_t[2] , v_t[2])
plt.xlabel("X(t)")
plt.ylabel("V(t)")
plt.title("Euler-Cromer")
plt.show()

plt.plot(x_t[3] , v_t[3])
plt.xlabel("X(t)")
plt.ylabel("V(t)")
plt.title("Velocity-Verlet")
plt.show()

plt.plot(x_t[4] , v_t[4])
plt.xlabel("X(t)")
plt.ylabel("V(t)")
plt.title("Beeman")
plt.show()

plt.plot(x_t[5] , v_t[5])
plt.xlabel("X(t)")
plt.ylabel("V(t)")
plt.title("Verlet")
plt.show()





