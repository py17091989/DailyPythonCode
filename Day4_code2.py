#Prime numbers stored in a list (in a given range)
start=int(input("Enter start number :"))
end=int(input("Enter end number :"))
#empty list to store prime numbers
prime_list=[ ]
for num in range(start,end+1):
    if num>1:
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
               break
        else:
            prime_list.append(num)
print(f"Prime numbers between {start} and {end} are :")
print(prime_list)