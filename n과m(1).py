import sys
input = sys.stdin.readline

def recur(number):
    if len(answer) == m:
        print(*answer)
        return
    for i in range(1, n+1):
        if i not in answer:
            answer.append(i)
            recur(number+1)
            answer.pop()


n, m = map(int, input().split())
answer = []
recur(1)