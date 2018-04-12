import sys
inFile = sys.stdin.readlines()
n = []
for l in inFile:
    n += l.strip().split()

words = dict()
for w in n:
    if w in words:
        words[w] += 1
    else:
        words[w] = 0

MyList = list(words)
print(MyList)
i = 0
for w in words:
    i += 1
    MyList[i - 1] = (words[w], w)

MegaList = sorted(MyList, key=lambda x: x[0], reverse=True)
print(*MegaList)
