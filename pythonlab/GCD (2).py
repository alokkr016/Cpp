
def find_gcd(a, b): 

    if a == 0 :

        return b 

     

    return find_gcd(b%a, a)



arr = [10,15,20]



num1 = arr[0]

num2 = arr[1]



gcd = find_gcd(num1, num2)



for i in range(2,len(arr)):

    gcd = find_gcd(gcd,arr[i])



print(gcd)
