"""
TODO: Write a description here
"""

import random

def main():
    count = 0
    while(count != 3):
    
        a = random.randint(10,99)
        b = random.randint(10,99)
        print("What is " + str(a) + " + " + str(b))
        c = int(input("Your answer: "))
        correct_answer = a + b
        if c  == correct_answer:
            count += 1
            print("Correct! You've gotten " + str(count) +" correct in a row.")
            
        else:
            print("Incorrect. The expected answer is " + str(correct_answer))
            count = 0
    print("Congratulations! You mastered addition.")
if __name__ == '__main__':
    main()
