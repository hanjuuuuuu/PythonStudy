import sys
from collections import deque
input = sys.stdin.readline
n, m, k, x = map(int, input().split())
distance = [0] * (n + 1)
visited = [False] * (n + 1)

graph = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                distance[i] = distance[v] + 1

    check = False
    for i in range(1, n+1):
        if distance[i] == k:
            print(i)
            check = True
    if check == False:
        print(-1)



bfs(x)