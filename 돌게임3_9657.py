import sys
input = sys.stdin.readline 

n = int(input())
dp = ['SK', 'CY', 'SK', 'SK', 'SK']
for i in range(5, n):
    if dp[i-1] == 'SK' and dp[i-3] == 'SK' and dp[i-4] == 'SK': 
        dp.append('CY') 
    else:
        dp.append('SK')
print(dp[n-1])
