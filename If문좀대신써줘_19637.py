import sys
input = sys.stdin.readline 

n, m = map(int, input().split())
fight_list = []
for i in range(n):
    name, up_limit = input().split(' ')
    fight_list.append([name, int(up_limit)])

for j in range(m):
    fight = int(input())
    start = 0
    end = len(fight_list) - 1
    
    while start <= end:
        mid = (start + end) // 2
        if fight <= fight_list[mid][1]:
            end = mid - 1
        else:
            start = mid + 1
    print(fight_list[start][0])