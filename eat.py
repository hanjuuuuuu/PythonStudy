import sys
input = sys.stdin.readline

T = int(input())

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1
    return start

for i in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    count = 0

    A.sort()
    B.sort()

    for j in A:
        count += binary_search(B, j, 0, M-1)
    print(count)
