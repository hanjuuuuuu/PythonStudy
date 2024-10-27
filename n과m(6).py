import sys
input = sys.stdin.readline

n, m = map(int, input().split())
number = list(map(int, input().split()))
number.sort()
answer = []

def recur(k):
    if len(answer) == m:
        print(*answer)
        return
    
    for i in range(k, n):
        answer.append(number[i])
        recur(i+1)
        answer.pop()

recur(0)
