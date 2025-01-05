import sys
input = sys.stdin.readline 

n, m = map(int, input().split())
height = list(map(int, input().split()))

start = 1
end = max(height)
answer = 0

while start <= end:
    mid = (start + end) // 2
    total = 0

    for h in height:
        if h > mid:
            total += h - mid
    
    if total >= m:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)
