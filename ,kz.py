import re
import collections
import sys
text = sys.stdin.readlines()
c = collections.Counter(re.findall(r'\w+', text)).most_common()
print(sorted(x for x, cnt in c if cnt == c[0][1])[0])
