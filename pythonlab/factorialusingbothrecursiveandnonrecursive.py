ch = int(input("Press 1 for recursive execution for factorial \nPress 2 for Non-recursive execution of factorial Algorithm "))
if ch == 1:
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
elif ch == 2:
    def factorial(n):
    factorial = 1
    if n < 0:
        print("Factorial of negative number doesnot exist")
    elif n == 1:
        print("Factorial of 1 is 1")
    else:
        for i in range(1, n+1):
            factorial = factorial*i
        print(factorial) 
 

n = int(input("Enter the number whose factorial you want "))
factorial(n)


else:
    exit
