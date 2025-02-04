import sys
input = sys.stdin.readline 

n, x = map(int, input().split())
visitor = list(map(int, input().split()))

if max(visitor) == 0:
    print('SAD')
    exit(0)

value = sum(visitor[:x])
answer = value
count = 1

# 슬라이딩 윈도우(이전 값을 활용하여 한칸씩 옆으로 옮겨가며 계산)
for i in range(x, n):
    value += visitor[i]
    value -= visitor[i-x]

    if value > answer:
        answer = value
        count = 1
    elif value == answer:
        count += 1

print(answer)
print(count)
