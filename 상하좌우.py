import sys
input = sys.stdin.readline

N = int(input())
plan = list(map(str, input().split()))
x, y = 1, 1

dx = [0,  0, -1, 1]
dy = [-1, 1, 0, 0]
case = ['L', 'R', 'U', 'D']

for i in plan:
    for j in range(len(case)):
        if i == case[j]:
            nx = x + dx[j]
            ny = y + dy[j]
    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue
    x = nx
    y = ny

print(x, y)
