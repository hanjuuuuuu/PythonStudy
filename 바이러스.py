import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def dfs(node):
    visited[node] = 1

    for nxt in graph[node]:
        if visited[nxt] == 1:
            continue
        dfs(nxt)


dfs(1)
print(sum(visited) - 1)
