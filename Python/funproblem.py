
# if the number is even, divide it  by 2
# if the number is odd, multiply by 3 and add 1
# guess: if we repeat this enough times, we'll always get to 1

# Collatz Conjecture 

# % gives the remainder of two whole numbers

def main():
    # ask user a whole number
    number = int(input("Enter a positive number: "))
    while number != 1:
        # if it's even
        if number % 2 == 0:
            number = number / 2
        else:
            number = number * 3 + 1
        print(number)

if __name__ == "__main__":
    main()
