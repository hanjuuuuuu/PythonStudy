import sys
input = sys.stdin.readline

S = input().rstrip()
arr = []
for i in range(len(S)):
    arr.append(S[i:len(S)+1])

print(*sorted(arr), sep='\n')
