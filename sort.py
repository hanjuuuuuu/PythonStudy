import sys
input = sys.stdin.readline

integer = list(map(int, input().split()))

print(*sorted(integer))