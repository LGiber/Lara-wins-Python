x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (y2 > y1) and (x1 != x2):
    if (x1+y1) % 2 == 0 and (math.fabs(x1-x2)+math.fabs(y1-y2)) % 2 == 0:
      print('YES')
else:
    print('NO')
