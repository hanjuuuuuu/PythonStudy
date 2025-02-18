import sys
import math
input = sys.stdin.readline 

n, m = map(int, input().split())
pack = []
one = []
for i in range(m):
    x, y= map(int, input().split())
    pack.append(x)
    one.append(y)
p = min(pack)
o = min(one) 

answer = min(n//6 * p + n%6 * o, (n//6 +1) * p, n*o)
print(answer)
