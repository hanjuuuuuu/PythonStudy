import sys
input = sys.stdin.readline

for i in range(1, 11):
    dump = int(input())
    height = list(map(int, input().split()))
    for j in range(dump):
        height.sort()
        max_value = height[-1]
        min_value = height[0]
        if max_value > min_value:
            height[-1] -= 1
            height[0] += 1
            height.sort()
    answer = height[-1] - height[0]
    print(f"#{i} {answer}")
