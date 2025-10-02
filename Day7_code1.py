#Star patterns------practice in for loop
#1. Left aligned triangle
for i in range(1,6):
      print("*"*i)
#*i repeat hota h in ascending order-
#2. Inverted triangle
for i in range(6,0,-1):
      print("*"*i)
#3. Right aligned triangle
for i in range(1,6):
      print(" " * (5-i)+ "*" *i)
#4. Pyramid pattern
for i in range(1,6):
    print(" " * (5-i) + "*" * ( 2 * i-1))
#5. Inverted pyramid
for i in range(6,0,-1):
    print(" " * (5-i)+ "*" * (2*i-1 ))
#"" space ke / 2*i-1 odd number star set
















