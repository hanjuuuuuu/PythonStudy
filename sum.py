import sys
input = sys.stdin.readline

for tc in range(1, 11):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

   # 행의 합
    max_row = 0
    for i in range(100):
        row = 0
        for j in range(100):
           row += arr[i][j]
        if max_row < row:
            max_row = row

    # 열의 합
    max_col = 0
    for i in range(100):
        col = 0
        for j in range(100):
            col += arr[j][i]
        if max_col < col:
            max_col = col

    # 대각선의 합
    max_cross = 0
    cross1 = 0
    cross2 = 0
    for i in range(100):
        cross1 += arr[i][i]
        cross2 += arr[i][99 - i]
        if max_cross < max(cross1, cross2):
            max_cross = max(cross1, cross2)

    print(f"#{tc} {max(max_row, max_col, max_cross)}")

