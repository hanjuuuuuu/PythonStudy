import sys
input = sys.stdin.readline

t = int(input())
check = ['a', 'e', 'i', 'o', 'u']

for i in range(1, t+1):
    words = input()
    answer = ""
    for word in words:
        if word not in check:
            answer += word
    print(f"#{i} {answer}")
