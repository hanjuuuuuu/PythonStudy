import sys
input = sys.stdin.readline

t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    price = list(map(int, input().split()))
    answer = 0

    max_price = price[-1]
    #n-1부터 0까지 -1씩 감소하면서 반복
    for i in range(n-1, -1, -1):
        if price[i] >= max_price:
            max_price = price[i]
        answer += max_price - price[i]

    print('#' + str(test_case) + ' ' + str(answer))
