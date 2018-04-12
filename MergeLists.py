A = list(map(int, input().split()))
B = list(map(int, input().split()))


def merge(A, B):
    i = 0
    j = 0
    c = []
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            c.append(A[i])
            i += 1
        else:
            c.append(B[j])
            j += 1
    while i < len(A):
        c.append(A[i])
        i += 1
    while j < len(B):
        c.append(B[j])
        j += 1
    return c

print(*merge(A, B), sep=" ")
