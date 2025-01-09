import sys
input = sys.stdin.readline 

dict = {}
n, m = map(int, input().split())
for _ in range(n):
    word = input().rstrip()

    if len(word) >= m:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
dict_key = list(dict.keys())
dict_key.sort(key = lambda x : (-dict[x], -len(x), x))

for answer in dict_key:
    print(answer)
