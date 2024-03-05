import sys
input = sys.stdin.readline

n = int(input())
student = []
for _ in range(n):
    score = input().split()
    student.append((score[0], int(score[1]), int(score[2]), int(score[3])))

student.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in student:
    print(i[0])
