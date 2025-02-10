import sys
input = sys.stdin.readline 

t = int(input())
for case in range(t):
    n, d = map(int, input().split(' '))
    answer = 0
    for i in range(n):
        v, f, c = list(map(int, input().split()))
        if f / c * v >= d:
            answer += 1
    print(answer)

