import numpy as np
import random as rn
import matplotlib.pyplot as plt


length = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
ln_saturation_time = [5.303, 5.749, 5.856, 6.132, 5.783, 6.354, 6.836, 6.713, 6.915, 7.456 ]
ln_saturation_w = [1.667, 1.895, 2.114, 2.343, 2.288, 2.390, 2.617, 2.536, 2.604, 2.760 ]


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
