import sys
input = sys.stdin.readline

#N을 M번 곱하는 재귀함수
def recur(n, m):
    if m == 0:
        return 1
    else:
        return n * recur(n, m-1)


for i in range(10):
    tc = int(input())
    n, m = map(int, input().split())
    answer = recur(n, m)
    print(f"#{tc} {answer}")
