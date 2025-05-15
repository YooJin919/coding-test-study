# 하루 지나면 익은 토마토와 상하좌우로 인접한 익지 않은 토마토가 익음 (BFS)
# 모든 토마토가 익는 최소 일수 출력

from sys import stdin
from collections import deque

m, n = map(int, stdin.readline().split())
d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
box = []
tomatoQueue = deque()
unripeCnt = 0
visited = [[False] * m for _ in range(n)]

for i in range(n):
  tomato = list(map(int, stdin.readline().split()))
  box.append(tomato)

for i in range(n):
  for j in range(m):
    if box[i][j] == 1:
      tomatoQueue.append([i,j])
    elif box[i][j] == 0:
      unripeCnt += 1

while(tomatoQueue):
  i, j = tomatoQueue.popleft()
  visited[i][j] = True
  for di, dj in d:
    ii = di + i
    jj = dj + j
    if 0 <= ii < n and 0 <= jj < m and box[ii][jj] == 0 and not visited[ii][jj]:
      box[ii][jj] = box[i][j] + 1
      tomatoQueue.append([ii, jj])
      unripeCnt -= 1

if unripeCnt > 0:
  print(-1)
else:
  res = 0
  for tmp in box:
    if res < max(tmp):
      res = max(tmp)
      
  print(res-1)