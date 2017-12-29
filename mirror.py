n = int(input())
n1 = str(n)
if len(n1) < 2:
    n1 = "0"+n1
if len(n1) < 3:
    n1 = "0"+n1
if len(n1) < 4:
    n1 = "0"+n1
n11 = (n1[0])
n2 = n1[1]
n3 = (n1[2])
n4 = n1[3]
if ((n11 == n4) and (n2 == n3)):
    print(1)
else:
    print(69)
