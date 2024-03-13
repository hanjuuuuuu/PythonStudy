import sys
input = sys.stdin.readline

s = input().rstrip()
d = [0] * 26

for i in s:
    d[ord(i)-97] += 1

print(*d)
