a = list(map(int, input().split()))
n = []
for i in range(a[1]):
    n.append(int(input()))
m = 0
b = sorted(n)
c = 0
while a[0] / b[c] >= 1:
    a[0] = a[0] - b[c]
    c += 1
    if c == a[1]:
        break
print(c)
