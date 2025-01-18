import sys
input = sys.stdin.readline 

n, k = map(int, input().split())
location = list(input())

answer = 0
for i in range(n):
    if location[i] == 'P':
        for j in range(i-k, i+k+1):
            if location[j] == 'H':
                location[j] = 0
                answer += 1
                break
print(answer)
