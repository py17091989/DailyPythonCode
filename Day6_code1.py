#Code for odd_even numbers with function
def even_odd_summary(start,end):
    even_list=[]
    odd_list=[]
    for num in range(start,end+1):
        if num%2==0:
            even_list.append(num)
        else:
            odd_list.append(num)
    return {"even_numbers":even_list,
           "odd_numbers":odd_list,
           "even_count":len(even_list),
           "odd_count":len(odd_list),
           "even_sum":sum(even_list),
           "odd_sum":sum(odd_list)}
#Driver code
start=int(input("Enter start number:"))
end=int(input("Enter end number:"))

summary=even_odd_summary(start,end)

print("\n---Results---")
print(f"Even numbers:{summary['even_numbers']}")
print(f"Odd numbers:{summary['odd_numbers']}")
print(f"Total even numbers:{summary['even_count']}")
print(f"Total odd numbers:{summary['odd_count']}")
print(f"Sum of even numbers:{summary['even_sum']}")
print(f"Sum of odd numbers:{summary['odd_sum']}")
