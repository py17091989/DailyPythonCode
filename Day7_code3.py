#Alphabet patterns
#1. A to E in each row :
for i in range (5):
    print("ABCDE")
#2. Increasing triangle of alphabets
for i in range(1,6):
    for j in range(i):
        print(chr(65+j),end=" ")
    print()
#3. Row wise increasing alphabets
ch=65
for i in range(1,6):
     for j in range(i):
         print(chr(ch),end=" ")
         ch +=1
     print( )
#4. Alphabet pyramid
for i in range(1,6):
    print(" " * (5-i), end=" ")
    for j in range(1,i+1):
        print(chr(64+j), end=" ")
    for j in range(i-1,0,-1):
        print(chr(64+j), end=" ")
    print ( )
#5. Right aligned alphabet
for i in range(1,6):
    print(" " * (5-i), end="")
    for j in range(i):
        print(chr(65+j),end="")
    print( )