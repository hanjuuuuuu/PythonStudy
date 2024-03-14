import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
btn = []
if m > 0:
    btn = list(input().split())

answer = abs(100 - n)  # + 또는 - 버튼으로 이동할 경우

for num in range(1000001):
    for i in str(num):
        if i in btn:    # 번호가 고장난 버튼에 포함되어 있을 때
            break
    # for문이 중간에 break 되지 않고 끝까지 실행됐을 경우
    # 번호를 누른 횟수 + 누른 번호부터 목표 N까지의 차이
    else:
        answer = min(answer, len(str(num)) + abs(num - n))

print(answer)
