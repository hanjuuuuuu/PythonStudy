import sys
input = sys.stdin.readline

def is_possible(location, height):
    if height - location[0] < 0:
        return False
    for i in range(1, m):
        if location[i] - location[i-1] > 2 * height:
            return False
    if n - location[-1] > height:
        return False
    return True

n = int(input())
m = int(input())
x = list(map(int, input().split()))

start = 1
end = n

answer = n
while start <= end:
    mid = (start + end) // 2
    if is_possible(x, mid):
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)
