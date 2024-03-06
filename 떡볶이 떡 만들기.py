import sys
input = sys.stdin.readline

n, m = map(int, input().split())
height = list(map(int, input().split()))

height.sort() # 10 15 17 19

# 최소 m만큼의 길이를 주기 위해서 절단기 높이
answer = 0
start = 0
end = height[-1]

while start <= end:
    mid = (start + end) // 2
    hap = 0
    for i in height:
        if i > mid:
            hap += i - mid
    if hap >= m:
        start = mid + 1
        answer = mid  # 최대한 덜 잘랐을 때가 정답이므로, 여기서 답 기록
    else:
        end = mid - 1

print(answer)
