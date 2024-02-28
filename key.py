import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    S = int(input())
    for i in range(2, 1000001):
        if S % i == 0:
            print("NO")
            break
        if i == 1000000:
            print("YES")