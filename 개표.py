import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    plus = int(n / 5)
    stick = n % 5
    for _ in range(plus):
        print("++++", end='')
    for _ in range(stick):
        print("|", end="")