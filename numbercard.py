import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
check = list(map(int, input().split()))

cards.sort()

cnt = {}
for card in cards:
    if card in cnt:
        cnt[card] += 1
    else:
        cnt[card] = 1

def binary_search(array, target):
    start = 0
    end = N - 1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return cnt.get(target)
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

for i in check:
    print(0 if binary_search(cards, i) == None else binary_search(cards, i), end=" ")

