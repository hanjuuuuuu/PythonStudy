import sys
input = sys.stdin.readline

N = int(input())
array = []
for i in range(N):
    array.append(list(map(int, input().split())))

for i in range(N-1):
    # 처음에 빨강 골랐을 때
    array[i+1][0] = min(array[i][1], array[i][2])+array[i+1][0]
    # 처음에 초록 골랐을 때
    array[i+1][1] = min(array[i][0], array[i][2])+array[i+1][1]
    # 처음에 파랑 골랐을 때
    array[i+1][2] = min(array[i][0], array[i][1])+array[i+1][2]

print(min(array[N-1][0], array[N-1][1], array[N-1][2]))