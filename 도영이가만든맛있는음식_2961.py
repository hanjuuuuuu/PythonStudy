import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
sour = []
bitter = []
answer = 1000000000

for _ in range(n):
    s, b = map(int, input().split())
    sour.append(s)
    bitter.append(b)

for i in range(1, n+1):
    com = list(combinations(list(range(n)), i))
    for food in com:
        s = 1
        b = 0
        for j in range(i):
            s *= sour[food[j]]
            b += bitter[food[j]]
        answer = min(answer, abs(s-b))

print(answer)


