import sys 
input = sys.stdin.readline 

n = int(input().rstrip())
answer = [0] * n
num = list(map(int, input().split()))

for i in range(n):
    count = 0
    for j in range(n):
        if num[i] == count and answer[j] == 0:
            answer[j] = i + 1
            break
        elif answer[j] == 0:
            count += 1

print(*answer)
