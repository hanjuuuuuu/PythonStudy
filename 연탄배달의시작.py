import sys
input = sys.stdin.readline

n = int(input())
place = list(map(int, input().split()))
minimum = 1000000
count = 0
for i in range(n-1):
    if place[i+1] - place[i] < minimum:
        minimum = place[i+1] - place[i]

for i in range(n-1):
    if place[i + 1] - place[i] == minimum:
        count += 1
print(count)
