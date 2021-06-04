#Write a function to flip a string by breaking it from the middle using string functions. (String should be broken from the middle and then two substrings should be reversed, in case of odd length string middle character will not change its position)
#Use case 1: CHANDIGARH --> DNAHCHRAGI
#Use case 2: UNIVERSITY --> EVINUYTISR
#Use case 3: MADAM --> AMDMA
#Use Case 4: GRADING --> ARGDGNI
def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str

def dhanchgarh(word):
    newword = ""
    n = len(word)
    if n % 2 == 0:
        newword = reverse(word[int(n/2):n-1]) + reverse(word[:int(n/2) + 1])
    else:
        newword = reverse((word[n/2 + 1:n-1])) + word[n/2] + reverse((word[:n/2 + 1]))
    print(newword)

dhanchgarh("Chandigarh")