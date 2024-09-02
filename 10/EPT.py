import numpy as np

#CONSTANTS:
sigma = 3.405 * 10**(-10) #[m]
mass = 6.63 * 10**(-26) #[kg]
epsilon = 1.653 * 10**(-21) #[J]
K_B = 1.381 * 10**(-23) #[(m^2*kg)/(Ks^2)]
R = 8.314 #[J/mol]
L = 30 #[sigma]
N = 100
N_A = 6.022 * 10**(23)

# in reduced units:

#for Temperature in terms of energy diagram: 
 #m = 0.007004253429765369 
 #b = 0.542270494392835 


#for pressure in terms of energy diagram: 
 #m = 0.0007875863978553718 
 #b = 0.05935291368858726 


#for pressure in terms of temperature in different energies diagram: 
 #m = 0.11243326373571985 
 #b = -0.0016134831195075536


Energy = [-7.36673297 , -3.51749685 , 0.63027188 , 5.21367245 , 11.46284989 ,
          17.54221057 , 22.4704125 , 32.70230889 , 44.07405081 , 50.44064173 ,
          57.89587499 , 73.43882987 , 78.79699055 , 92.50258288 , 90.20172009] 


temperature = [0.53833627 , 0.52454693 , 0.57322736 , 0.5806873 , 0.61870749 ,
               0.64452158 , 0.67235763 , 0.74607889 , 0.8362792 , 0.86109013 ,
               0.9294205 , 1.04859536 , 1.1042971 , 1.22190974 , 1.20182879] 


pressure =  [0.05884174 , 0.05738494 , 0.06280713 , 0.06367209 , 0.06795455 ,
             0.07087835 , 0.07400903 , 0.08224619 , 0.09244166 , 0.09523403 ,
             0.10289048 , 0.11632618 , 0.12256791 , 0.13576008 , 0.13343772]

m1 , c1 = np.polyfit(temperature , pressure , 1)
print("m1 =", m1)
print("c1 =", c1)

for i in range (len(pressure)):
    pressure[i] = (pressure[i]*epsilon)/(sigma*sigma)
    temperature[i] = (temperature[i]*epsilon)/K_B

m , c = np.polyfit(temperature , pressure , 1)
print("m =", m)
print("c =", c)

V = (L*L*sigma*sigma*N_A)/N
print ("V =", V)

b = V - (R/m)
print ("b =", b)

a = - c * V**2
print ("a =", a)


