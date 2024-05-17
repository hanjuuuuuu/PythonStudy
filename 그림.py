from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pic = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
def bfs(y, x):
    picarea = 1
    queue = deque()
    queue.append((y, x))
    while queue:
        ey, ex = queue.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0 <= ny < n and 0 <= nx < m:
                if pic[ny][nx] == 1 and visited[ny][nx] == False:
                    picarea += 1
                    visited[ny][nx] = True
                    queue.append((ny, nx))
    return picarea


cnt = 0
maxv = 0
for j in range(n):
    for i in range(m):
        if pic[j][i] == 1 and visited[j][i] == False:
            cnt += 1  # 그림 개수 증가
            visited[j][i] = True  # 방문 처리
            maxv = max(maxv, bfs(j, i))

print(cnt)
print(maxv)
