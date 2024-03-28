import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    x, y = map(int,input().split())
    arr.append([x, y])

arr.sort(key=lambda a: a[1])
print(*arr[0])
