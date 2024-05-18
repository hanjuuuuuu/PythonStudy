import sys
input = sys.stdin.readline

n, m = map(int, input().split())
number = list(map(int, input().split()))
number.sort()

answer = []
def recur():
    if len(answer) == m:
        print(*answer)
        return

    for i in number:
        if i not in answer:
            answer.append(i)
            recur()
            answer.pop()


recur()
