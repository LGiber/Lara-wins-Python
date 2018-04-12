print(min(map(int, input().split()), key=lambda x: (x % 2 == 0, x)))
