import sys
input = sys.stdin.readline 

n, m = map(int, input().split())

keyword = set([input().rstrip() for _ in range(n)])

for _ in range(m):
    upload = set(input().rstrip().split(','))
    keyword -= upload
    print(len(keyword))
