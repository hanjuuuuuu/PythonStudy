import sys
input = sys.stdin.readline 

dict = {}
t =  int(input())
for _ in range(t):
    n, k, t, m = map(int, input().split())
    scores_arr = [[0 for _ in range(k+1)] for _ in range(n+1)]
    cnt_d = {}
    last_d = {}
    for submit in range(m):
        i, j, s = map(int, input().split())
        if scores_arr[i][j] < s:
            scores_arr[i][j] = s
        if i in cnt_d:
            cnt_d[i] += 1
        else:
            cnt_d[i] = 1
        last_d[i] = submit
    res = sorted(cnt_d.items(), key=lambda x: (-sum(scores_arr[x[0]]), x[1], last_d[x[0]]))
    ranking = 1
    for team in res:
        if team[0] == t:
            print(ranking)
            continue
        ranking += 1
        