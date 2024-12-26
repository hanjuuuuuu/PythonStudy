import sys
input = sys.stdin.readline 

def sum(num):
    total = 0
    for i in num:
        if i.isdigit():
            total += int(i)
    return total

n = int(input())
arr = []
answer = []
for i in range(n):
    guitar = int(input())
    arr.append(guitar)

arr.sort(key=lambda x: (len(x), sum(x), x))
for i in arr:
    print(i)