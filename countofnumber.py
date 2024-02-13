import sys
input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())

nums = str(A * B * C)

for i in range(10):
    print(nums.count(str(i)))

