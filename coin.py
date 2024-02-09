import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = []

#n만큼 돌면서 리스트에 추가하고
#리스트 돌면서 몫, 나머지 구하기

for i in range(N):
    A.append(int(input()))
A.sort(reverse=True)

count = 0
for coin in A:
    count += K // coin
    K %= coin

print(count)