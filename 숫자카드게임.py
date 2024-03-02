import sys
input = sys.stdin.readline

N, M = map(int, input().split())

answer = 0
for i in range(N):
    card = list(map(int, input().split()))
    # min_value = min(card)
    # answer = max(answer, min_value)
    card.sort()
    if card[0] > answer:
        answer = card[0]

print(answer)



