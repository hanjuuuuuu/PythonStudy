import sys
input = sys.stdin.readline

def palindrome(n):
    length = (len(n)-1) // 2
    if n == n[::-1]:
        if n[:length] == n[:length][::-1] and n[length+1:] == n[length+1:][::-1]:
            return "YES"
    else:
        return "NO"
    return "NO"


t = int(input())
for i in range(1, t+1):
    s = input().rstrip()
    print(f"#{i} {palindrome(s)}")
