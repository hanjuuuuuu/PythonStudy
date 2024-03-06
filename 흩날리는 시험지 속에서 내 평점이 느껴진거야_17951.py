import sys
input = sys.stdin.readline

n, k = map(int, input().split())
x = list(map(int, input().split()))

# n을 k개의 그룹으로 나눠서 각 그룹의 합 중 최소값이 가장 큰 수 구하기
