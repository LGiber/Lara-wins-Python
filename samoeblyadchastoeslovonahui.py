from collections import Counter

data = open("input.txt").read().split()
with open("output.txt", "w") as out:
    out.write(sorted(Counter(data).items(), key=lambda x: (-x[1], x[0]))[0][0])
