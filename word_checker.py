import sys
input = sys.stdin.readline

N = int(input())
count = N
for i in range(N):
    group_word = input()
    for j in range(len(group_word)-1):
        if group_word[j] == group_word[j+1]:
            continue
        elif group_word[j] in group_word[j+1:]:
            count -= 1
            break


print(count)