import sys
input = sys.stdin.readline

words = input().split('-')
answer = ''.join(word[0] for word in words)
print(answer)