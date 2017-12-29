s = input()
pos = s.find('f')
if (s.count('f')) == 1:
        print("-1")
elif (s.count('f')) == 0:
        print("-2")
elif (s.count('f')) > 1:
    print(s.find('f', pos + 1))
