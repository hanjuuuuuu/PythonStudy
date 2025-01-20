import sys
input = sys.stdin.readline 

n = int(input())
dp = ['sk', 'cy', 'sk', 'sk', 'sk']
for i in range(5, n):
    if dp[i-1] == 'sk' and dp[i-3] == 'sk' and dp[i-4] == 'sk': 
        dp.append('cy') 
    else:
        dp.append('sk')
print(dp[n-1])

