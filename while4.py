x = int(input())
xMax = x
while x != 0:
    if x > xMax:
        xMax = x
    x = int(input())
    if x == 0:
        break
print(xMax)
