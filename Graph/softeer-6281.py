# 격자 N * M
# 얼음 1, 빈칸 0
# 얼음이 녹는데 걸리는 시간 출력
# 녹는 기준 = 얼음 4면 중 2면이 외부 노출 -> 1시간 뒤 녹음
# BFS 1바퀴 = 1시간 -> 얼음이 아니라 빈 곳을 큐에 넣고 돌림 -> 빈 곳이랑 연결됐는데 얼음이라면 +1 -> bfs 한 바퀴 돌고 2라면 삭제

from sys import stdin
from collections import deque

res = 0
move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
n, m = map(int, stdin.readline().split())
grid = []
iceNum = 0

for _ in range(n):
  iceList = list(map(int, stdin.readline().split()))
  iceNum += iceList.count(1)
  grid.append(iceList)

def bfs():
  global iceNum
  q = deque()
  q.append((0, 0)) # (0, 0)은 항상 빈 곳
  visited = [[0] * m for _ in range(n)] # 외부 공기 노출 체크
  visited[0][0] = -1
  
  while(q):
    x, y = q.popleft()
    
    for mx, my in move:
      xx = x + mx
      yy = y + my
      
      if(0 <= xx < n and 0 <= yy < m):
        if(grid[xx][yy] == 1): # 얼음
          visited[xx][yy] += 1
        elif(grid[xx][yy] == 0 and not visited[xx][yy]): # 얼음 아니고 확인 안함
          visited[xx][yy] = 1
          q.append((xx, yy))

  for i in range(n):
    for j in range(m):
      if(visited[i][j] >= 2 and grid[i][j] == 1): # 외부 공기 2면 이상 노출
        grid[i][j] = 0 # 얼음 녹이기
        iceNum -= 1

while(1):
  if(iceNum == 0):
    break
  res += 1
  bfs()
  
print(res)