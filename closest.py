N = int(input())
a = [int(i) for i in input().split()]
x = int(input())
b = [abs(a[i]-x) for i in range(len(a))]
print(a[b.index(min(b))])
