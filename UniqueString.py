n=input("Enter your string :")
j=" "
for i in n:
    if i not in j:
        j += i
        print(i)