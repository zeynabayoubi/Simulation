import numpy as np
import random as rn
import matplotlib.pyplot as plt


M = np.zeros((20 , 200)) #Main array
M[19][:] = 1

for j in range (1000):

    x = rn.randint(0,199)
    print ("x= ",x)
    y = 9

    for i in range (2000):
    
        c = rn.randint(1,4)
    
        if c==1:# 1 is up
            print ("c=1")
            y-=1
        
            if y<=0:
                break
            if M[y-1][x]==1 or M[y+1][x]==1 or M[y][(x-1)%200]==1 or M[y][(x+1)%200]==1:
                M[y][x]=1
                break    
        
        if c==2: # 2 is right
            print ("c=2")
            x+=1
            x = x%200 #border conditions for x axis has been considered periodic

            if M[y-1][x]==1 or M[y+1][x]==1 or M[y][(x-1)%200]==1 or M[y][(x+1)%200]==1:
                M[y][x]=1
                break

        if c==3: # 3 is down
            print ("c=3")
            y+=1

            if M[y-1][x]==1 or M[y+1][x]==1 or M[y][(x-1)%200]==1 or M[y][(x+1)%200]==1:
                M[y][x]=1
                break

        if c==4: # 4 is left
            print ("c=4")
            x-=1
            x = x%200  #border conditions for x axis has been considered periodic

            if M[y-1][x]==1 or M[y+1][x]==1 or M[y][(x-1)%200]==1 or M[y][(x+1)%200]==1:
                M[y][x]=1
                break

print (M)
plt.imshow(M, cmap='magma')
plt.show()


        

