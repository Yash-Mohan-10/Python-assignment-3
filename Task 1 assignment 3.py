def factorial(n):
    if(n==1 or n==0):
        return 1
    else:
        return factorial(n-1)*n

a=int(input("Enter a number: "))
b=factorial(a)
print("Factorial of",a,"is:",b)