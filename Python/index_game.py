"""
this game is called index game
"""
import random
def ask_4_index(data):
    n = len(data)
    index = random.randint(0,n-1)
    while True:
        val = input("Who is at index " + str(index)+ ": ")
        if val == data[index]:
            print("Good Job")
            break
        print("Not correct Try again")
def main():
    data = ["Jason", "Raven", "Obama", "Alok"]
    print(data)
    ask_4_index(data)
if __name__ == "__main__":
    main()