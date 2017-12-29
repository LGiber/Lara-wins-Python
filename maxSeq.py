max = 0
maxSeq = 0
i = -1
while i != 0:
    i = int(input())
    if i > max:
        max, maxSeq = i, 1
    elif i == max:
        maxSeq += 1
print(maxSeq)
