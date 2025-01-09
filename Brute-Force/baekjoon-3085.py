# N X N 크기에 사탕 채우기
# 사탕 색 모두 같지 않을 수 있음
# 1. 사탕의 색이 다른 인접한 2칸 고름
# 2. 고른 칸에 들어있는 사탕을 교환 (자리 이동)
# 3. 모두 같은 색으로 이루어진 가장 긴 연속 부분을 먹음
# 먹을 수 있는 가장 긴 연속 부분의 개수 반환

from sys import stdin

n = int(stdin.readline().rstrip())
board = []
max = 0
dxdy = [[0, 1], [1, 0]] # 오른쪽, 아래만 확인해도 모두 확인 가능

for _ in range(n):
  board.append(list(stdin.readline().rstrip()))
  
def checkSequence():
  res = 0
  for i in range(n):
    curR = 1
    curC = 1
    for j in range(n-1):
      # 가로 확인
      if board[i][j] == board[i][j+1]:
        curR += 1
      else:
        if curR > res:
          res = curR
        curR = 1
      # 세로 확인
      if board[j][i] == board[j+1][i]:
        curC += 1
      else:
        if curC > res:
          res = curC
        curC = 1
        
    if curC > res:
      res = curC
    if curR > res:
      res = curR
  return res

for i in range(n):
  for j in range(n):
    for d in dxdy:
      tmp = 0
      ii = i + d[0]
      jj = j + d[1]
      if 0 <= ii < n and 0 <= jj < n:
        if board[i][j] != board[ii][jj]:
          board[ii][jj], board[i][j] = board[i][j], board[ii][jj]
          tmp = checkSequence()
          if tmp > max:
            max = tmp
          board[ii][jj], board[i][j] = board[i][j], board[ii][jj]
          
print(max)