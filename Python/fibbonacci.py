num1 = 0
num2 = 1

n = int(input("How many number in Fibbonacci series you want "))
print(num1, num2, end = ' ')
while(n > 2):
    fibo = num1 + num2
    num1 = num2
    num2 = fibo
    print(fibo,end = ' ')
    n -= 1

