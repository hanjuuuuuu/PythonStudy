import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a.sort()


def binary(target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if target == a[mid]:
            return 1
        elif target > a[mid]:
            start = mid + 1
        elif target < a[mid]:
            end = mid - 1
    return 0


for num in b:
    left = 0
    right = n-1
    print(binary(num, left, right))