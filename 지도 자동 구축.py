import sys

input = sys.stdin.readline

n = int(input())


def dot(n):
    if n == 0:
        return 2
    else:
        return dot(n - 1) + dot(n - 1) - 1


print(dot(n) * dot(n))
