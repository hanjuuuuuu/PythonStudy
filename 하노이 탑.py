import sys
input = sys.stdin.readline

def hanoi(k, start, end, mid):
    if k == 1:
        print(start, end)
        return
    hanoi(k-1, start, mid, end)
    print(start, end)
    hanoi(k-1, mid, end, start)

n = int(input())
print(2**n-1)
if n <= 20:
    hanoi(n, 1, 3, 2)
