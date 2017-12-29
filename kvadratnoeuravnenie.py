a = float(input())
b = float(input())
c = float(input())
D = (b ** 2) - (4 * a * c)
if D == 0:
    x = (0 - b) / (2 * a)
    print(x)
elif D > 0:
    x1 = (((0 - b) + (D ** 0.5)) / (2 * a))
    x2 = (((0 - b) - (D ** 0.5)) / (2 * a))
    if x1 > x2:
        print(x2, x1)
    else:
        print(x1, x2)
