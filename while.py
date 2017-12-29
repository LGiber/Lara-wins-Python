n = int(input())
i = 1
while n != 0:
    print(i ** 2, end=" ")
    i = i + 1
    if n < (i ** 2):
        break
