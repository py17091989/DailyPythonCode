#prime numbers in a given range with count and sum
start=int(input("Enter start number :"))
end=int(input("Enter end number :"))
prime_list=[ ]

for num in range(start,end+1):
     if num>1:
         for i in range(2,int(num**0.5)+1):
             if num%i==0:
                 break
         else:
              prime_list.append(num)
#print prime numbers
print(f"Prime numbers between {start} and {end} are :")
print(prime_list)
#Count of prime numbers
prime_count=len(prime_list)
print(f"Sum of prime numbers:{prime_count}")
#Sum of prime numbers
prime_sum=sum(prime_list)
print(f"sum of prime numbers:{prime_sum}")

