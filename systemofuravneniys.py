a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

if (a == 0 and c == 0) or (b == 0 and d == 0):
    print()
elif a == 0:
    y = e / b
    x = (f - d * y) / c
else:
    y = ((f * a - e * c) / (d * a - b * c))
    x = ((e - b * y) / a)
print(x, y)
