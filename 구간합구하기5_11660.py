import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
prefix = [[0 for _ in range(n+1)] for _ in range(n+1)]

for x in range(n):
    for y in range(n):
        prefix[x+1][y+1] = prefix[x][y+1] + prefix[x+1][y] - prefix[x][y] + arr[x][y]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    answer = prefix[x2][y2] - prefix[x2][y1-1] - prefix[x1-1][y2] + prefix[x1-1][y1-1]
    print(answer)


