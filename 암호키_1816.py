import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    S = int(input())
    # 모든 소인수가 1,000,000 보다 크면 YES, 그렇지 않으면 NO 출력
    answer = 1
    for i in range(2, 1000001):
        if S % i == 0:
            answer = 0
            break
    if answer == 1:
        print("YES")
    else:
        print("NO")