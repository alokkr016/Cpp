

def main():
    # milestone1
    stone = 20
    player = 1
    while(stone != 0):
               
        if(player == 1 and stone != 0):
            print("There are " + str(stone) + " stones left")            
            print("Player "+ str(player) + " would you like to remove 1 or 2 stones? ",end="")
            c = int(input())
            if c == 1 or c == 2:
                stone -= c
                player = 2
                print(end="\n")
            
            else:
                while c != 1 and c != 2:
                    c = int(input("Please enter 1 or 2: "))
                stone -= c
                player = 2
                print(end="\n")
        
        if(player == 2 and stone != 0):
            print("There are " + str(stone) + " stones left")           
            print("Player "+ str(player) + " would you like to remove 1 or 2 stones? ",end="")
            c = int(input())
            if c == 1 or c == 2:
                stone -= c
                player = 1
                print(end="\n")
            else:
                while c != 1 and c != 2:
                    c = int(input("Please enter 1 or 2: "))
                stone -= c
                player = 1
                print(end="\n")
    print("Player " + str(player)+ " wins!")
if __name__ == '__main__':
    main()