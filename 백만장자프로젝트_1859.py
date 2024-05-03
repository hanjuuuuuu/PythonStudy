import sys
input = sys.stdin.readline

t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    price = list(map(int, input().split()))
    answer = 0
    for _ in range(n):




    print('#' + str(test_case) + ' ' + str(answer))