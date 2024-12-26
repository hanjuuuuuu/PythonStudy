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
for _ in range(n):
    guitar = input().rstrip()
    arr.append(guitar)

arr.sort(key=lambda x: (len(x), sum(x), x))
for i in arr:  
    print(i)
    