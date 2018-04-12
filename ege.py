fin = open("input.txt", "r", encoding="utf-8")
fout = open("output.txt", "w", encoding="utf-8")


def SBall(line):
    tmpList = []
    for i in map(str, line[:-1].split(" ")):
        if i.isdigit():
            if int(i) < 40:
                return 0
            tmpList.append(int(i))
    return sum(tmpList)


man = []
text = fin.readlines()
k = int(text[0])
#  print(k)
for line in text[1:]:
    #  print(line)
    man.append(SBall(line))
man.sort()
man.reverse()
#  print(man)
if man[k] == 0:
    print(0, file=fout)
elif man[0] == man[k]:
    print(1, file=fout)
elif man[k] == man[k-1]:
    maxBall = 0
    while True:
        if man[k - 1] != man[k - 2]:
            maxBall = man[k - 2]
            break
        k -= 1
    print(maxBall, file=fout)
else:
    print(man[k-1], file=fout)
fin.close()
fout.close()
