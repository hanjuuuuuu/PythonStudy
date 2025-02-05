import sys
input = sys.stdin.readline 

s = list(input())
zero = s.count("0") // 2
one = s.count("1") // 2

for _ in range(one):
    idx = s.index("1")
    s.pop(idx)

s = s[::-1]
for _ in range(zero):
    idx = s.index("0")
    s.pop(idx)

s=s[::-1]
print(''.join(s))
