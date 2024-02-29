import sys
input = sys.stdin.readline

n = int(input())
d = [0] * 91
d[1] = 1
d[2] = 1
def fibo(x):
    for i in range(3, n+1):
        d[i] = d[i-1] + d[i-2]
    return d[x]


print(fibo(n))
