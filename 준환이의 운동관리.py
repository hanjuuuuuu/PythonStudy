import sys
input = sys.stdin.readline

t = int(input())

for test_case in range(1,t+1):
    L,U,X = map(int, input().split())
    answer = 0
    if X < L:
        answer = L-X
    elif X > U:
        answer = -1
    else:
        answer = 0
    print(f"#{test_case} {answer}")
