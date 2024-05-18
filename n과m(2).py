import sys
input = sys.stdin.readline

n, m = map(int, input().split())
answer = []

def recur(number):
    if len(answer) == m:
        print(*answer)
        return
    for i in range(number, n+1):
        if i not in answer:
            answer.append(i)
            recur(i+1)
            answer.pop()


recur(1)
