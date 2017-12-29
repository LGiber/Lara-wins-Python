a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
delta = a * d - b * c
dX = d * e - b * f
dY = a * f - c * e
x = dX / delta
y = dY / delta
print(x, y)
