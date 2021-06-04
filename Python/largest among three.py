a, b, c = map(int, input("Enter three number separated by space ").split())
if a > b and a > c:
    print("%d is largest than other two number" % a)
elif b > c:
    print("%d is larger than other two number" % b)
else:
    print("%d is largest among all three" % c)
