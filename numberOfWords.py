import sys
import re
print(len(set(re.findall('[^ \n]+', sys.stdin.read()))))
