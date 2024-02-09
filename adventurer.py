import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
num.sort()

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in num:
    count += 1
    if count >= i:
        result += 1
        count = 0


print(result)

