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
