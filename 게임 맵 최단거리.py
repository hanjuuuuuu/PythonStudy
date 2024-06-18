from collections import deque


def solution(maps):
    n = len(maps)
    m = len(maps[0])

    # 상하좌우
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))

    # 상대방 진영에 방문한 적 없으면 -1
    if maps[n - 1][m - 1] == 1:
        return -1

    # 상대방 진영에 방문했다면 최솟값 반환
    else:
        return maps[n - 1][m - 1]