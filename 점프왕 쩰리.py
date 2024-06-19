from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
map = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

# 아래와 오른쪽만 이동 가능
dx = [1, 0]
dy = [0, 1]


def bfs(start_x, start_y):
    queue = deque()
    queue.append([start_x,start_y])

    while queue:
        x, y = queue.popleft()

        for i in range(2):
            nx = x + dx[i] * map[x][y]
            ny = y + dy[i] * map[x][y]

            if 0<=nx<n and 0<=ny<n:
                if not visited [nx][ny]:
                    visited[nx][ny] = True
                    queue.append([nx, ny])

    if visited[n - 1][n - 1]:
        print('HaruHaru')
    else:
        print('Hing')


bfs(0,0)


