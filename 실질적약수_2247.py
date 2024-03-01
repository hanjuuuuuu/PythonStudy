import sys
input = sys.stdin.readline

n = int(input())
d = [0] * (n+1)

cnt = 0
for i in range(2, int(n**0.5)+1):
    if i == n:
        break
    if n % i == 0:
        cnt += i
        if i != n // i:
            cnt += n // i
    d[i] += cnt
    print('k', cnt)

print('d',d)
print(sum(d) % 1000000)

