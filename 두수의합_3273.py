import sys
input = sys.stdin.readline

n = int(input())
a = sorted(list(map(int, input().split())))
x = int(input())

answer = 0
left = 0
right = n-1

while left < right:
    total = a[left] + a[right]
    if total == x:
        answer +=1
        left += 1
    elif total > x:
        right -= 1
    else:
        left += 1
print(answer)
