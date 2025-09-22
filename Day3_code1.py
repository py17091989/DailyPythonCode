#prime number checker
#User se number input lena
num=int(input("Enter any number :"))
#prime number check logic
if num>1:
    for i in range(2,num):
        if num%i==0:
            print(num,"is not a prime number")
            break
    else:
         print(num,"is a prime number")

