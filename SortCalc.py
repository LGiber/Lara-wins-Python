A = list(map(int, input().split()))


def CountSort(A):
    A = list(map(int, input().split()))
    gades = [0] * 101
    for now in A:
        gades[now] += 1
    for gade in range(len[gades]):
        for i in range(gades[gade]):
            print(gade, end = " ")

print(CountSort(A))


