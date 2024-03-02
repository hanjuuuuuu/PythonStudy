import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort(reverse=True)

# 가장 큰 수를 K번 더하고 두 번째로 큰 수를 한번 더하기
answer = 0

# 가장 큰 수가 더해지는 횟수
count = M // (K + 1) * K
count += M % (K + 1)

answer += count * arr[0]    # 가장 큰 수 더하기
answer += (M - count) * arr[1]  # 두 번째로 큰 수 더하기

print(count)

