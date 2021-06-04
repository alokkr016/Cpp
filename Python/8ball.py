"""
Simulates a magic eight ball.
Prompts the user to type a yes or no question and gives
a random answer from a set of prefabricated responses.
"""

import random

def main():
    # ask user for a question
    question = input("Enter a yes or no question: ")
    while question != "stop":
        # roll a four-sided die
        random_variable = random.randint(1, 4)
        if random_variable == 1:
            print("Definitively yes.")
        if random_variable == 2:
            print("Absolutely not. Not a chance.")
        if random_variable == 3:
            print("Don't count on it...")
        if random_variable == 4:
            print("Only time will tell.")
        question = input("Enter another yes or no question: ")


if __name__ == "__main__":
    main()
