import sys
input = sys.stdin.readline 

s, e, q = input().split()

# 시간을 정수로 표현
s = int(s[:2]+s[3:])
e = int(e[:2]+e[3:])
q = int(q[:2]+q[3:])

answer = 0
arr = set()

while True:
    try:
        time, nickname =  input().split()
        time = int(time[:2] + time[3:])

        if time <= s :
            arr.add(nickname)
        elif e <= time <= q and nickname in arr:
            arr.remove(nickname)
            answer += 1
    except:
        break
    
print(answer)

