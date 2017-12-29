import sys
import re
strWords = ''
a = sys.stdin.readlines()
for line in a:
    strWords = strWords + ' ' + line.replace('\n', '')

d = {}
for i in strWords:
    for word in input().split():
        d[word] = d.get(word, 0) + 1

for i in sorted(d.items(), key=lambda x: (x[0])):
    if i[1] == max(d.values()):
        print(i[0])
        break
