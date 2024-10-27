import sys
input = sys.stdin.readline

n, m = map(int, input().split())
number = list(map(int, input().split()))
number.sort()

answer=[]
def recur(start):
    if len(answer) == m:
        print(*answer)
        return
    for i in number:
        answer.append(i)
        recur(i)
        answer.pop()
    
recur(0)
