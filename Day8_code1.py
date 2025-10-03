#1. Even numbers from 1 to 20
for i in range (2,20,2):
     print(i, end= " ")
print( )
#2. Odd numbers from 1 to 20
for i in range (1,20,2):
    print(i,end=" ")
print()
#3. Sum of 1 to n
n=10
total=0
for i in range(1,n+1):
    total +=i
print("sum :",total)
#4. Factorial of a number
n=5
fact=1
for i in range(1,n+1):
    fact *=i
print("factorial :",fact)
#5. Table of a number
n=9
for i in range(1,11):
    print(f"{n}*{i}={n*i}")