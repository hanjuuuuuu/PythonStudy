import sys
input = sys.stdin.readline

n = input().rstrip()
t = len(n) // 2
a = 0
b = 0

for i in range(t):
    a += int(n[i])

for i in range(t, len(n)):
    b += int(n[i])

if a == b:
    print("LUCKY")
else:
    print("READY")
