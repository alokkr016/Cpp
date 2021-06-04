while True:    
    ch = input("Press 1 for recursive execution for factorial \nPress 2 for Non-recursive execution of factorial Algorithm ")
    if ch == '1':
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
    elif ch == '2':
        def factorial1(n1):
            fact1 = 1
            if n1 < 0:
                print("Factorial of negative number doesnot exist")
            elif n1 == 1:
                print("Factorial of 1 is 1")
            else:
                for i1 in range(1, n1+1):
                    fact1 = fact1*i1
                print(fact1) 
    

        n1 = int(input("Enter the number whose factorial you want "))
        factorial1(n1)


    else:
        exit

