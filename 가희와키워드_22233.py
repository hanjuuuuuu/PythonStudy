import sys
input = sys.stdin.readline 

n, m = map(int, input().split())

keyword = []
upload = []

for _ in range(n):
    keyword.append(input().rstrip())

keyword = set(keyword)

for _ in range(m):
    upload = list(input().rstrip().split(','))
    keyword = keyword - set(upload)
    print(len(keyword))


