#-----------------------------Nested Loops-------------
#1. Solid square
for i in range (5):
    print("*"* 5)
#2. Rectangle (3*6)
for i in range (3):
      print("*" * 6)
#3. Hollow Square
n=5
for i in range (5):
    for j in range (n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#4. Hollow Right Triangle
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        if j==1 or i==j or i==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
 #5.Floyd's Triangle
n=1
for i in range(1,6):
     for j in range(1,i+1):
         print(n,end=" ")
         n +=1
     print( )

