import sys
input = sys.stdin.readline()

x = int(input[1])
y = ord(input[0]) - ord('a') + 1

dx = [-1, 1, -1, 1, 2, 2, -2, -2] # 123
dy = [2, 2, -2, -2, 1, -1, 1, -1] # abc

count = 0
for i in range(8):
  nx = x + dx[i]
  ny = y + dy[i]
  if nx > 8 or ny > 8 or nx < 1 or ny < 1:
      continue
  else:
      count += 1
print(count)
