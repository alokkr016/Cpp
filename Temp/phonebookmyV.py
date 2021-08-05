def make_a_phonebook():
    my_phonebook = {}
    
    while True:
        name = input("Enter the name of the person: ")
        if name == "":
            break
        age = input("Enter the phone number of the person: ")
        my_phonebook[name] = age

    return my_phonebook

def print_phonebook(name):
    for i in name:
        print(i, "->", name[i])        



def main():
    
    name =  make_a_phonebook()
    print_phonebook(name)


if __name__ == "__main__":
    main()