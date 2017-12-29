n = int(input())
i = 0
while n <= 9 and i <= n:
    print('+___ '*i)
    print('|', i, ' /', sep='', end=' ')
    print()
    print(('|__\\ ')*i)
    print(('|    ')*i)
    i += 1
