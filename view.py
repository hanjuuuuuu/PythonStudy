import sys
input = sys.stdin.readline

for i in range(1, 11):
    n = int(input())
    height = list(map(int, input().split()))
    answer = 0

    for j in range(2, n-2):
        check = height[j]
        neighbor = max(height[j-2], height[j-1], height[j+1], height[j+2])

        if check > neighbor:
            answer += check - neighbor

    print(f"#{i} {answer} ")
