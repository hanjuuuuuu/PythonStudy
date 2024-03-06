import sys
input = sys.stdin.readline

n = int(input())
n_type = list(map(int, input().split()))
m = int(input())
m_type = list(map(int, input().split()))

n_type.sort() # 2 3 7 8 9
m_type.sort() # 5 7 9

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for i in m_type:
    if binary_search(n_type, i, 0, len(n_type)-1) == None:
        print('no', end=' ')
    else:
        print('yes', end=' ')
