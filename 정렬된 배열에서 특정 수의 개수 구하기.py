import sys
input = sys.stdin.readline

n, x = map(int, input().split())
arr = list(map(int, input().split()))

# x가 등장하는 마지막 인덱스에서 처음 인덱스 빼면 몇 개 있는지 확인 가능

def first_index(array, target, start, end):
    result = -1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            result = mid
            end = mid - 1
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return result


def last_index(array, target, start, end):
    result = -1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            result = mid
            start = mid + 1
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return result


def count_x(array, x):
    last = last_index(array, x, 0, len(arr)-1)
    first = first_index(array, x, 0, len(arr)-1)
    if first == -1 or last == 1:
        return -1
    else:
        return last - first + 1


print(count_x(arr, x))
