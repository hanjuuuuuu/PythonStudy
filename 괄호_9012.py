import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    stack = []
    p = input()
    for j in p:
        if j == '(' :
            stack.append(j)
        elif j == ')':
            if len(stack) == 0:
                stack.append(')')
                break
            else:
                stack.pop()
        
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')
