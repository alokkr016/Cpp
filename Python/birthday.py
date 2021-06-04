def have_birthday(ages, name):
    print("You are one year older ",name)
    ages[name] += 1


def main():
    ages = {'Chris': 33, 'Julie': 22, 'Mehran': 50}
    print(ages)
    have_birthday(ages,"Chris")
    print(ages)
    
if __name__ == "__main__":
    main()