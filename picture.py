"""
1. 아이디어
-2중 for문 => 값 1 && 방문ㅌ => BFS
-BFS 돌면서 그림 개수 +1

2. 시간복잡도
- BFS: 0(V+E)
- V: 500 * 500
- E: 4 * 500 * 500
- V+E: 5 * 250000 = 100만 < 2억 가능!

3. 자료구조
-그래프 전체 지도: int[][]
-방문: bool[][]
-Queue(BFS)
"""

import sys
input = sys.stdin.readline()

n, m = map(int, input())
map = [list(map(int, input().split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]

cnt = 0
max
for