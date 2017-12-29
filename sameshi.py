a = int(input())
c = 1
b = 0
while a != 0:
    d = int(input())
    a, d = d, a
    if d == a:
        c += 1
    if c > b:
        b = c
    if a != d:
        c = 1
print(b)
