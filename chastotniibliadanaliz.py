from collections import Counter
import sys
a = sys.stdin.readlines()
words = []
for _ in a:
    words.extend(input().split())

counter = Counter(words)
pairs = [(-pair[1], pair[0]) for pair in counter.most_common()]
words = [pair[1] for pair in sorted(pairs)]
print('\n'.join(words))
