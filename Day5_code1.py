#Even and Odd numbers in a range with counts and sums
start=int(input("Enter start number:"))
end=int(input("Enter end number:"))
#even and odd  numbers ki list
even_list=[]
odd_list=[]
#check numbers in range
for num in range(start,end+1):
    if num%2==0:
        even_list.append(num)
    else:
        odd_list.append(num)
#print results
print(f"Even numbers between {start} and {end} are :{even_list}")
print(f"Odd numbers between {start} and {end} are:{odd_list}")
#count
print(f"Total even numbers:{len(even_list)}")
print(f"Total odd numbers:{len(odd_list)}")
#sums
print(f"Sum of all even numbers are:{sum(even_list)}")
print(f"Sum of all odd numbers are:{sum(odd_list)}")
