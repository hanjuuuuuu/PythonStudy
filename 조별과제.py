import sys
input = sys.stdin.readline

t = int(input())
for i in range(1, t+1):
    student = int(input())
    answer = student // 3
    print(f"#{i} {answer}")