import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    data = input().split()
    arr.append((data[0], int(data[1])))

arr = sorted(arr, key=lambda student: student[1])

for student in arr:
    print(student[0], end=' ')
