n = str(input())
if int(n[-1]) == 0 or (5 <= int(n[-1]) <= 9) or (10 <= int(n) <= 20):
    print(n, 'korov')
elif 2 <= int(n[-1]) <= 4:
    print(n, 'korovy')
else:
    print(n, 'korova')
