import numpy as np
from PIL import Image


def c (n,r):
    if (r==0):
        return 1;
    if (r>n):
        return 0;
    return (c(n-1,r) + c(n-1,r-1));

n=int(input("Enter the number: "))
x=np.zeros((n,2*n-1))

for i in range (n):
    for j in range (n):
        if c(i,j)>0:
            x[i][2*j + (n-(i+1)) ] = c(i,j)%2
#print(x)

y=np.zeros([n , 2*n-1 , 3] , dtype=np.uint8)
for i in range (n):
    for j in range (2*n-1):
        if x[i][j]==1:
            y[i][j] = [0,0,255]
        else:
            y[i][j] = [255,128,0]
Image.fromarray(y)
