import sys
input = sys.stdin.readline

e, s, m = map(int, input().split())

answer = 1
a, b, c = 1, 1, 1
while True:
    if a == e and b == s and c == m:
        print(answer)
        break
    else:
        a += 1
        b += 1
        c += 1
        answer += 1
    if a > 15:
        a = 1
    if b > 28:
        b = 1
    if c > 19:
        c = 1

