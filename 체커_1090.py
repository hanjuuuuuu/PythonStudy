import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
# [[15, 14], [15, 16], [14, 15], [16, 15]]

for i in range(1, N+1):
    # i개가 모이도록 하는 최소 횟수 출력

# X, Y 구분해서 계산한 후에 합쳐서 최솟값 알려주기
# 비용을 최소화하려면 우리의 집 중 한 곳에서 모이기
# 가까운 두명의 거리만 더하기