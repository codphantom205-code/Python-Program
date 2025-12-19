a=int(input("Enter a number : "))
b=int(input("Enter a number : "))
even_square = {x**2 for x in range (a,b+1) if x%2 ==0}
print(even_square)
