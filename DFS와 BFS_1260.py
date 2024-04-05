from collections import deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited1 = [0 for _ in range(n+1)]
visited2 = [0 for _ in range(n+1)]


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()


def dfs(node):
    visited1[node] = True
    print(node, end=' ')
    for i in graph[node]:
        if not visited1[i]:
            dfs(i)


def bfs(node):
    queue = deque([node])
    visited2[node] = True
    while queue:
        k = queue.popleft()
        print(k, end=' ')
        for i in graph[k]:
            if not visited2[i]:
                queue.append(i)
                visited2[i] = True

dfs(v)
print()
bfs(v)

