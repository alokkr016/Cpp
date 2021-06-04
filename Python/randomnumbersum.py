"""
Prints out a randomly generated addition problem
and checks if the user answers correctly.
"""

import random 

def main():
    a = random.randint(10,99)
    b = random.randint(10,99)
    print("What is " + str(a) + " + " + str(b))
    c = int(input("Your answer: "))
    correct_answer = a + b
    if c  == correct_answer:
        print("Correct!")
    else:
        print("Incorrect. The expected answer is " + str(correct_answer))
    

if __name__ == '__main__':
    main()