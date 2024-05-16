import sys
input = sys.stdin.readline

# 완전이진트리이므로 n개 // 2 까지 연산자이고, 나머지 리프노트는 숫자여야함
for i in range(1, 11):
    n = int(input())
    oper = n // 2
    operator = ['+', '-', '*', '/']
    answer = 1
    for j in range(n):
        tc = input().split()
        if int(tc[0]) <= oper:
            if tc[1] not in operator:
                answer = 0
        else:
            if tc[1] in operator:
                answer = 0

    print(f"#{i} {answer}")




