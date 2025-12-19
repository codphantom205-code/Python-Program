l=eval(input("Enter the list : "))
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
print(l1)
