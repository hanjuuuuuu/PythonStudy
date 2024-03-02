import sys
input = sys.stdin.readline

N, K = map(int, input().split())
temp = list(map(int, input().split()))

# 누적합
prefix = [0] * (N+1)
for i in range(N):
    prefix[i+1] = prefix[i] + temp[i]

# 누적합에서 연속적인 온도의 합 구하기
answer = []
for i in range(K, N+1):
    answer.append(prefix[i] - prefix[i-K])

print(max(answer))
