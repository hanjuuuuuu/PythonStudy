import sys
input = sys.stdin.readline

for i in range(10):
    tc = int(input())
    string = input().rstrip()
    sentence = input().rstrip()

    cnt = sentence.split(string)
    print(sentence, cnt)
    print(f"#{tc} {len(cnt)-1}")