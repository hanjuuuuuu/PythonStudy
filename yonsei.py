import sys
input = sys.stdin.readline

N = int(input())

count = 0
i = 1
while N - 2 * i >= 4:
    count += (N - 2 * i) // 2 - 1
    i += 1

print(count)

