#count prime numbers in given numbers
start=int(input("Enter start number :"))
end=int(input("Enter end number:"))
count=0
for num in range(start,end+1):
    if num>1:
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                break
        else:
            count+=1
print(f"Total prime numbers between {start} and {end} :{count}")




