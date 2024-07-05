import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []
for i in range(n):
    x = int(input().rstrip())
    if x != 0:
        heapq.heappush(heap, (-x, x))
    else:
        if len(heap) >= 1:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
