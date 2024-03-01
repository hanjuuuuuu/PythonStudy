import sys
input = sys.stdin.readline

k = int(input())
answer = []
for i in range(2, int(k**0.5)+1):
    while k % i == 0:
        answer.append(i)
        k //= i

if k != 1:
    answer.append(k)

print(len(answer))
print(*answer)
