import numpy as np
import random as rn
import matplotlib.pyplot as plt

x=np.zeros(200)
for i in range (200):
    x[i]=i
    
y=np.zeros(200)
hbar=np.zeros(4000)
h2bar=np.zeros(4000)

for i in range (1000):
    c=rn.randint(0,199)
    y[c]+=1
    hbar[i]=hbar[i-1]+1
    sum=0
    for j in range (200):
        sum+= y[j]**2
    h2bar[i]=sum
    
plt.plot(x,y)


for i in range (1000):
    c=rn.randint(0,199)
    y[c]+=1
    hbar[i+1000]=hbar[(i+1000)-1]+1
    sum=0
    for j in range (200):
        sum+= y[j]**2
    h2bar[i+1000]=sum
    
plt.plot(x,y)


for i in range (1000):
    c=rn.randint(0,199)
    y[c]+=1
    hbar[i+2000]=hbar[(i+2000)-1]+1
    sum=0
    for j in range (200):
        sum+= y[j]**2
    h2bar[i+2000]=sum

plt.plot(x,y)


for i in range (1000):
    c=rn.randint(0,199)
    y[c]+=1
    hbar[i+3000]=hbar[(i+3000)-1]+1
    sum=0
    for j in range (200):
        sum+= y[j]**2
    h2bar[i+3000]=sum

plt.plot(x,y)   
plt.legend(["Dataset 1", "Dataset 2", "Dataset 3", "Dataset 4"])
plt.xlabel('length')
plt.ylabel('height')
plt.show()


hbar=hbar/200
h2bar=h2bar/200

t=np.zeros(4000)
for i in range (4000):
    t[i]=i+1

plt.plot(t,hbar)
plt.xlabel('period of time')
plt.ylabel('hbar')
plt.xticks([0,1000,2000,3000,4000] , ['0','1000','2000','3000','4000'])
period_of_time=[0,1000,2000,3000,4000]
h_bar=[0,5,10,15,20]
plt.scatter(period_of_time,h_bar)
plt.show()

w_t=np.zeros(4000)
for i in range (4000):
    w_t[i]= (h2bar[i] - hbar[i]**2 )**(1/2)

ln_w_t=np.zeros(4000)
ln_t=np.zeros(4000)

for i in range (4000):
    ln_w_t[i]=np.log(w_t[i])
    ln_t[i]=np.log(t[i])
    
plt.plot(t,w_t)
plt.xlabel('time')
plt.ylabel('w_t')
plt.show()

plt.plot(ln_t,ln_w_t)
plt.xlabel('ln(time)')
plt.ylabel('ln(w_t)')
#plt.scatter(ln_t,ln_w_t)
plt.show()


m,b=(np.polyfit(ln_t,ln_w_t,1))
print("beta= ",m)



