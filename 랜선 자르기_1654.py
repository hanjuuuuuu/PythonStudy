import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lan = []
for _ in range(n):
    lan.append(int(input()))

start = 1
end = max(lan)
while start <= end:
    mid = (start + end) // 2
    lines = 0
    for i in lan:
        lines += i // mid
    if lines >= k:
        start = mid + 1
    else:
        end = mid - 1
print(end)
