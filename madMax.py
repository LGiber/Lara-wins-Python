a = list(map(int, input().split()))
maximum = max(a)
for i in range(len(a)):
    if a[i] == maximum:
        index = i
print(maximum, index)
