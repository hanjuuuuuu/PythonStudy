import sys
import math
input = sys.stdin.readline

h, w, n, m = map(int, input().split())
x = math.ceil(w / (m+1))
y = math.ceil(h / (n+1))
print(x * y) 