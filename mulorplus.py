import sys
input = sys.stdin.readline

S = input()

result = int(S[0])

for i in range(1, len(S)):
    num = int(input[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
print(result)