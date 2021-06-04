n = 4
count = 0
disp = 0
for i in range(1,n+1):
    count += i
    disp = count
    for j in range(1,i+1):
        print(disp,end=" ")
        disp = disp - 1
    print(end='\n')
