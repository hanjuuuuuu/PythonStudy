import sys
input = sys.stdin.readline
from bisect import bisect_left

T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    count = 0

    A.sort()
    B.sort()

    for j in range(N):
        count += bisect_left(B, A[j])

    print(count)