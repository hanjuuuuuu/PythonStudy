import sys
input = sys.stdin.readline
M, N = map(int, input().split())
arr = list(map(int, input().split()))

start = 1
end = max(arr) 
res = 0 

while start <= end:
    mid = (start + end) // 2
    total = 0

    for x in arr:
        if x >= mid:
            total += (x // mid) 

    if total >= M:
        start = mid + 1 
        res = mid 
    else:
        end = mid - 1 

print(res)