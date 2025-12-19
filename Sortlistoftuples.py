a=int(input("Enter number of tuples:\n"))
tuple_list=[]
for i in range(a):
    print(f"\nEnter value for tuple {i+1} ")
    b=input("First element : ")
    c=input("Second element : ")
    tuple_list.append((b,c))
sorted_list=sorted(tuple_list,key=lambda X:X[1])
print("\nSorted list based on second element :")
for y in sorted_list:
     print(y)
