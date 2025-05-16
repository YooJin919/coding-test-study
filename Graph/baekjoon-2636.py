# 공기와 인접한 치즈는 1시간 후에 녹아 사라짐 (BFS)
# 치즈 없는 칸 0, 치즈 있는 칸 1
# 모든 치즈가 녹아 사라지는 데 걸리는 시간, 모든 치즈가 녹기 1시간 전 존재한 치즈 개수 출력

from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
board = deque()
d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
time = 0
cheeseCnt = 0
air = deque() # 공기 위치 (중간 구멍 제외)
cheese = deque() # 1시간 후에 사라질 치즈

for _ in range(n):
  input = list(map(int, stdin.readline().split()))
  board.append(input)
  cheeseCnt += input.count(1)

def meltCheese(cheese):
  global board
  for i, j in cheese:
    board[i][j] = 0

def findMeltingCheese(): # 1시간 후에 사라질 치즈 찾기
  global board, d, time, air, cheese, cheeseCnt
  visited = [[False] * m for _ in range(n)]
  air.clear()
  cheese.clear()
  air.append((0, 0))
  visited[0][0] = True
  
  while(air):
    i, j = air.popleft()
    for di, dj in d:
      ii = i + di
      jj = j + dj
      if 0 <= ii < n and 0 <= jj < m and not visited[ii][jj]:
        visited[ii][jj] = True
        if board[ii][jj] == 0:
          air.append((ii, jj))
        else:
          cheese.append((ii, jj))
    
  meltCheese(cheese)
  cheeseCnt -= len(cheese)
  time += 1
    
while(cheeseCnt > 0):
  findMeltingCheese()

print(time)
print(len(cheese))