a = int(input())
b = int(input())
k = a // b
print('YES'*(((a//b)-(a % b))//(a//b))+'NO'*((((a % b)+2)//((a % b)+1)) % 2))