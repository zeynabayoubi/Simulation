import colorama
from colorama import Fore
colorama.init(autoreset=True)

def c (n,r):
    if (r==0):
        return 1;
    if (r>n):
        return 0;
    return c(n-1,r) + c(n-1,r-1);

n=int(input("Enter the number:"));




for i in range (n):
    for j in range (n-(i+1)):
        print (end=" ")
    for j in range (i+1):
        if (c(i,j)//2)==0:
            print(Fore.WHITE + ".", end=" ")
        else:
             print('.', end=" ")
    print();



