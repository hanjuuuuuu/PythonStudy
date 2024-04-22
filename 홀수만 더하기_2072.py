import sys

input = sys.stdin.readline

T = int(input())

for test_case in range(1, T + 1):
    num = list(map(int, input().split()))
    hap = 0
    for i in num:
        if i % 2 == 1:
            hap += i

    print('#' + str(test_case) + ' ' + str(hap))
