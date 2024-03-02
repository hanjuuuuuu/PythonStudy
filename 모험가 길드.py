import sys
input = sys.stdin.readline

N = int(input())
fear = list(map(int, input().split()))
fear.sort()

group = 0  # 그룹의 수
count = 0  # 모험가 수
for i in fear:
    count += 1
    if count >= i:
        group += 1
        count = 0

print(group)
