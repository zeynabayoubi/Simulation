import numpy as np
import random as rn
import matplotlib.pyplot as plt


length = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
ln_saturation_time = [5.303, 5.872, 6.613, 6.886, 7.083, 7.077, 7.240, 7.274, 7.534, 7.527]
ln_saturation_w = [0.777, 1.054, 1.291, 1.537, 2.203, 1.675, 1.654, 1.777, 1.643, 1.721]


plt.scatter(np.log(length) , ln_saturation_time )
plt.plot(np.log(length) , ln_saturation_time )
plt.xlabel('ln(length)')
plt.ylabel('ln(saturation time)')
plt.show()
m1 , b1 = np.polyfit( np.log( length) , ln_saturation_time , 1)
print("z= " , m1)


plt.scatter(np.log(length) , ln_saturation_w )
plt.plot(np.log(length) , ln_saturation_w )
plt.xlabel('ln(length)')
plt.ylabel('ln(saturation w)')
plt.show()
m2 , b2 = np.polyfit(  np.log(length) , ln_saturation_w , 1)
print("alpha= " , m2)
