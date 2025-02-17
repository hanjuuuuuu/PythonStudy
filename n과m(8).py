import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
answer = []

def recur(k):
    if len(answer) == m:
        print(*answer)
        return

    for i in range(k, n):
        answer.append(arr[i])
        recur(i)
        answer.pop()
recur(0)
