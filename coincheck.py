import sys
input = sys.stdin.readline

N, M = map(int, input().split())
array = []
for i in range(N):
    array.append(int(input()))

d = [10001] * (M+1)

d[0] = 0
for x in array:
    if M % x == 0:
        return