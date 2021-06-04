def my_mean(l):
    n = len(l)
    total_sum = sum(l)
    mean_my = total_sum/n
    print("Mean is " + str(mean_my))
def my_meadian(l):
    n = len(l)
    l.sort()
    if n % 2 == 0:
        median1 = l[n//2]
        median2 = l[n//2 - 1]
        median = (median1 + median2)/2
    else:
        median = l[n//2]
    print("Median is: " + str(median))

def my_mode(y):
    y.sort()
    L1=[]

    i = 0
    while i < len(y) :
    	L1.append(y.count(y[i]))
    	i += 1

    d1 = dict(zip(y, L1))
    d2={k for (k,v) in d1.items() if v == max(L1) }
    print("Mode(s) is/are :" + str(d2))   
        

my_num = [3,7,5,8,4,4,4,3,1,2,6,7]
while(True): 
    print("What do you want to do ")
    print("Press 1 for mean \nPress 2 for median\nPress 2 for Mode\nPress 4 to exit the program")
    value = input("Enter your choice ")
  
    if value == '1':
        my_mean(my_num)
    if value == '2':
        my_meadian(my_num)
    if value == '3':
        my_mode(my_num)
    if value == '4':
        exit()
