"""
Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.
"""

MARS_CONVERT = 0.378

def main():
    # convert string to float (number with decimals) 
    weight = float(input("Enter your weight: "))
    # convert earth weight to mars weight
    mars_weight = weight * MARS_CONVERT
    print("Your weight on Mars is " + str(mars_weight))
    

if __name__ == "__main__":
    main()


