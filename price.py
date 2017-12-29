import math
n = float(input())
rub = int((int(n) * 100) // 100)
kop = int(round(n % 1, 2) * 100)
print(int(rub), int(kop))
