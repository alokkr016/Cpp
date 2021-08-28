def factorial(n):
    
    if n > 1:
        return n*factorial(n - 1)
    else:
        return 1
    
n = int(input("Enter a number whose factorial you want to print "))
if n < 0:
    print("Factorial doesn't exist for negative number")
elif n == 0:
    print("1")
else:
    print(factorial(n))