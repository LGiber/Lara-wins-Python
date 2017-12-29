n = int(input())
t1 = "The next number for the number"
t2 = "The previous number for the number"
next = t1 + " " + str(n) + " " + "is" + " " + str(int(n + 1)) + "."
prev = t2 + " " + str(n) + " " + "is" + " " + str(int(n - 1)) + "."
print(next, prev, sep='\n')
