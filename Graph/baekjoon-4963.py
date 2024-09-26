# 섬의 개수 출력
# 가로, 세로, 대각선에 이어진 지역 == 같은 섬
# BFS

from sys import stdin
from collections import deque

d = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, 1], [1, -1], [-1, -1]]

def countIsland(y, x, sea, visited, w, h):  
  q = deque()
  q.append((y, x))
  visited[y][x] = True
  
  while(q):
    curY, curX = q.popleft()
    for [dy, dx] in d:
      nowY = curY + dy
      nowX = curX + dx
      
      if 0 <= nowY < h and 0 <= nowX < w:
        if not visited[nowY][nowX] and sea[nowY][nowX]:
          visited[nowY][nowX] = True
          q.append((nowY, nowX))
  
while(1):
  w, h = map(int, stdin.readline().split())
  if w == 0 and h == 0:
    break
  
  cnt = 0
  sea = []
  visited = [[False] * w for _ in range(h)]
  
  for _ in range(h):
    sea.append(list(map(int, stdin.readline().split())))
    
  for i in range(h):
    for j in range(w):
      if sea[i][j] and not visited[i][j]:
        countIsland(i, j, sea, visited, w, h)
        cnt += 1

  print(cnt)