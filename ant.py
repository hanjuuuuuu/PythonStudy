import sys
input = sys.stdin.readline

N = int(input())
K = list(map(int, input().split()))

# 계산 결과 저장 하기 위한 DP 테이블 초기화
d = [0] * 100

d[0] = K[0]
d[1] = max(K[0], K[1])
for i in range(2, N):
    d[i] = max(d[i - 1], d[i - 2] + K[i])

print(d[N - 1])