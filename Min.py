i = list(input().split())
max = 1000
for k in range(len(i)):
    s = int(i[k])
    if (s < max)and(s > 0):
        max = s
print(max)
