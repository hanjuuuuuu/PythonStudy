import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
visited = [0 for _ in range(m)]

for _ in range(n):
    graph = [[] for _ in range(m)]

dx = []
dy = []
def bfs(node):
    visited[node] = True
    for i in range graph[node]:
        if not v
