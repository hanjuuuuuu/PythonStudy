import sys
input = sys.stdin.readline

t = int(input().rstrip())
for i in range(1, t+1):
    n = int(input())
    income = list(map(int, input().split()))
    aver = 0
    answer = 0
    for k in income:
        aver += k
    for j in income:
        if j <= aver//len(income):
            answer += 1
    print(f"#{i} {answer}")