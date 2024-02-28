import sys
input = sys.stdin.readline

N = int(input())

hint = [list(map(str, input().split())) for _ in range(N)]

answer = 0

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            cnt = 0

            if a == b or b == c or c == a:
                continue

            # 숫자가 정해졌다면
            for arr in hint:
                number = list(arr[0])
                strike = int(arr[1])
                ball = int(arr[2])

                strike_count = 0
                ball_count = 0

                # 스트라이크 계산
                if a == int(number[0]):
                    strike_count += 1
                if b == int(number[1]):
                    strike_count += 1
                if c == int(number[2]):
                    strike_count += 1

                # 볼 계산
                if a == int(number[1]) or a == int(number[2]):
                    ball_count += 1
                if b == int(number[0]) or b == int(number[2]):
                    ball_count += 1
                if c == int(number[0]) or c == int(number[1]):
                    ball_count += 1

                if ball == ball_count and strike == strike_count:
                    cnt += 1

            if cnt == N:
                answer += 1
print(answer)
