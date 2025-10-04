#1. Diamond Pattern
n=5
for i in range(1,n+1):
    print(" " * (n-i)+ "*" * (2*i-1))
for i in range(n-1,0,-1):
    print(" " * (n-i)+ "*" * (2*i-1))

#2. Pascal Triangle
from math import comb
n=5
for i in range (n):
    print(" " * (n-i),end=" ")
    for j in range (i+1):
        print(comb(i,j),end=" ")
    print( )

#3. Checkerboard pattern (X-0)
for i in range (5):
    for j in range (5):
        if (i + j) % 2 == 0:
            print("X",end=" ")
        else:
            print("0",end=" ")
    print( )
#4. Hourglass pattern
n=5
for i in range(n,0,-1):
    print(" " * (n-i) + "*" * (2*i-1))
for i in range(2,n+1):
    print(" " * (n-i) + "*" * (2*i-1))

#5.Binary Triangle
for i in range(1,6):
    for j in range(1,i+1):
        print((i+j) % 2,end=" " )
    print()

