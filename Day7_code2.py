#Number pattens in for loop
#1. 1 to 5 in each row
for i in range (5):
    print(12345)
#2. Increasing triangle of numbers
for i in range (1,6):
    for j in range(1,i+1):
        print( j, end="")
    print( )
#3.Reverse numbers in each row
for i in range(5):
    print(54321)
#4. Row wise increasing numbers
num=1
for i in range (1,6):
    for j in range (i):
        print(j,end=" ")
        num += 1
    print ( )
#5. Centred number pyramid
for i in range (1,6):
    print( " " * (5-i),end=" ")
    for j in range(1,i+1):
        print(j, end= " ")
    for j in range(i-1,0,-1):
        print(j, end=" ")
    print ( )