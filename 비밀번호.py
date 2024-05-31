import sys
input = sys.stdin.readline


for j in range(1, 11):
    n, m = input().split()
    answer = []
    for i in m:
        if len(answer) == 0:
            answer.append(i)
        else:
            if i == answer[-1]:
                answer.pop()
            else:
                answer.append(i)

    a = ''.join(answer)
    print(f'#{j} {a}')
