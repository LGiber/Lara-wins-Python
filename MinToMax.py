a = [int(i) for i in input().split()]
for i in range(len(a)):
    if a[i] == max(a):
        index_max = i
    if a[i] == min(a):
        index_min = i
a[index_max], a[index_min] = a[index_min], a[index_max]
print(' '.join(str(i) for i in a))
