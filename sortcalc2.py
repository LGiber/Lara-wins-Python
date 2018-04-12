A = list(map(int, input().split()))


def CountSort(A):
    counts = [0 for i in range(101)]

    for i in A:
        counts[i] += 1

        A = []

    for i in range(101):
        A.extend([i for j in range(counts[i])])

    return A


print(*CountSort(A))
