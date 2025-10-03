#---------------=====-----while Loop practice---------
#1. print 1 to 10
i=1
while i<=10:
    print(i,end=" ")
    i +=1
print()
#2. Sum of digits
n=1234
sum_digits=0
while n>0:
     sum_digits += n%10
     n//=10
print("sum is :",sum_digits)
#3. Reverse a number
n=1234
rev=0
while n>0:
    rev=rev*10 + n%10
    n//=10
print("Reversed :",rev)
#4.Palindrome number
n=121
original=n
rev=0
while n>0:
    rev=rev*10+n%10
    n//=10
if rev==original:
    print("Palindrome")
else:
    print("Not Palindrome")

#5. Armstrong number
n=153
original=153
sum=0
while n>0:
    digit=n%10
    sum +=digit **3
    n//=10
if sum==original:
    print("Yes,it is an armstrong number")
else:
    print("No, It is not an Armstrong number")