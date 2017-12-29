a = int(input())
b = int(input())
c = int(input())

if (a > b):
    if (b > c):
        print(a, b, c)
    else:
        print(a, c, b)
elif (b > a):
    if (a > c):
        print(b, a, c)
    else:
        print(b, c, a)
elif (c > a):
    if (a > b):
        print(c, a, b)
else:
    print(c, b, a)
