import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)

for i in range(1, n+1):
    time, count, *pre = map(int, input().split())
    dp[i] = time
    for j in pre:
        dp[i] = max(dp[i], dp[j]+time)
print(max(dp))