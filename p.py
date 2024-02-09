import sys

read = sys.stdin.readline

N = int(read().rstrip())

nums = [0] * 10001

for _ in range(N):
    num = int(read().rstrip())
    nums[num] += 1

for i in range(1, 10001):
    if nums[i]:
        for _ in range(nums[i]):
            print(i)
