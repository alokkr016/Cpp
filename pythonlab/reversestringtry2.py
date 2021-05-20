#Use case 1: CHANDIGARH --> DNAHCHRAGI
#Use case 1: CHANDIGARH --> DNAHCHRAGI
#Use case 2: UNIVERSITY --> EVINUYTISR
#Use case 3: MADAM --> AMDMA
#Use Case 4: GRADING --> ARGDGNI
def dhandigarh(word):
    newword = ""
    newword = word[::-1]
    n = len(newword)
    if n % 2 == 0:
        newword2 = newword[int(n/2):n+1] + newword[0:int(n/2)]
    else:
        newword2 = newword[int(n/2) + 1 : n + 1] +newword[int(n//2)] + newword[0 : int(n/2)]
    print(newword2)

while(1):
    print("please enter your word")
    word = input()

    
    
    