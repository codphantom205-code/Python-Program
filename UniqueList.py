l = input("Enter your list : ")
l = [eval(x) for x in l.split(',')]  

l1 = []
for i in l:
    if i not in l1:
        l1.append(i)

print( l1)
