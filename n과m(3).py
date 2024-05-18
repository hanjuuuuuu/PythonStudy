import sys
input = sys.stdin.readline

n, m = map(int, input().split())
answer = []


def recur():
    if len(answer) == m:
        print(*answer)
        return

    for i in range(1, n+1):
        answer.append(i)
        recur()
        answer.pop()


recur()
