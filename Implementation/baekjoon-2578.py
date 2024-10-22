from sys import stdin

board = []
order = []
for _ in range(5):
  board.append(list(map(int, stdin.readline().split())))
for _ in range(5):
  order += list(map(int, stdin.readline().split()))

def checkBingo():
  global board
  cnt = 0
  isLine = False
  
  for i in range(5):
    for j in range(5):
      if board[i][j] == 0:
        # 대각선 1
        if i == j:
          for l in range(5):
            if board[l][l] == 0:
              isLine = True
            else:
              isLine = False
              break
          if isLine:
            cnt += 1
            isLine = False
        # 대각선 2
        if i + j == 4:
          for l in range(5):
            if board[l][4-l] == 0:
              isLine = True
            else:
              isLine = False
              break
          if isLine:
            cnt += 1
            isLine = False
        # 가로 줄
        for l in range(5):
          if board[i][l] == 0:
              isLine = True
          else:
            isLine = False
            break
        if isLine:
          cnt += 1
          isLine = False
        # 세로 줄
        for l in range(5):
          if board[l][j] == 0:
              isLine = True
          else:
            isLine = False
            break
        if isLine:
          cnt += 1
          isLine = False
  if cnt >= 12:
    return True
  return False

def markNumber(num):
  global board
  for i in range(5):
    for j in range(5):
      if board[i][j] == num:
        board[i][j] = 0
  return

for i in range(25):
  markNumber(order[i])
  if checkBingo():
    print(i + 1)
    break