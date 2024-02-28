import sys
input = sys.stdin.readline

a, b, c, d, e, f = map(int, input().split())
y = (c * d - a * f) // (b * d - a * e)
x = (c * e - b * f) // (a * e - b * d)

print(x, y)