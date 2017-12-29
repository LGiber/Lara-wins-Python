import sys
import re
strWords = ''
a = sys.stdin.readlines()
for line in a:
    strWords = strWords + ' ' + line.replace('\n', '')

print(len(set(strWords.split())), sep='', end='')
