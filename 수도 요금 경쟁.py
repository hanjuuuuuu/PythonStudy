import sys
input = sys.stdin.readline

t = int(input())
for i in range(1, t+1):
    p, q, r, s, w = map(int, input().split())
    a = p * w
    if w <= r:
        b = q
    else:
        b = q + s * (w - r)

    print(f'#{i} {min(a, b)}')
