"""
Number Guesser Program

This is an example of how to use variables to 
keep track of information in a program that 
also makes use of loops
"""
import random

UPPER_LIMIT = 100
LOWER_LIMIT = 0
def main():
    ul = UPPER_LIMIT
    ll = LOWER_LIMIT
    entered_num = int(input("Enter your number "))
    try1 = 0
    
    while True:
        
        random_numb = random_num(ll,ul)
        check = checker(ll,ul,random_numb,entered_num)
        print("this is check number ",check)
        try1 += 1
        if random_numb == entered_num:
            break

    print("Total number of try is ",try1)
    print("your number is ",random_numb)
        

        


def checker(ll,ul,random_numb,entered_num):
    if random_numb < entered_num:
        ll = random_numb
        return random_numb, ll
    if random_numb > entered_num:
        ul = random_numb
        return random_numb, ul
     
    


def random_num(a,b):
     
    return random.randint(a,b)
if __name__ == "__main__":
    main()