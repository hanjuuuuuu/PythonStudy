import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a, b, d = map(int, input().split())

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
case = [3, 2, 1, 0]  # 서,남,동,북

# 방문 처리
dp = [[0] * m for _ in range(n)]
dp[a][b] = 1

# 왼쪽 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


info = []
for _ in range(n):
    info.append(list(map(int, input().split())))
    for i in range(len(case)):
        nx = a + dx[i]
        ny = b + dy[i]
        if nx =