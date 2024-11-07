# 통로 근처에 음식물이 떨어져있음
# 근처에 있는 음식물은 뭉쳐서 하나의 큰 음식물이 됨
# 떨어진 음식물 중 가장 큰 음식물의 크기 구하기

from sys import stdin
from collections import deque

n, m, k = map(int, stdin.readline().split())
path = [[0] * m for _ in range(n)]
trash = []
d = [[0, 1], [0, -1], [1, 0], [-1, 0]]

for _ in range(k):
  r, c = map(int, stdin.readline().split())
  path[r-1][c-1] = 1
  
def bfs(i, j):
  q = deque()
  q.append((i, j))
  cnt = 1
  
  while(q):
    curI, curJ = q.popleft()
    for di, dj in d:
      ii = curI + di
      jj = curJ + dj
      if 0 <= ii < n and 0 <= jj < m:
        if path[ii][jj]:
          q.append((ii, jj))
          path[ii][jj] = 0
          cnt += 1
  return cnt
  
for i in range(n):
  for j in range(m):
    if path[i][j]:
      path[i][j] = 0
      trash.append(bfs(i, j))
      
print(max(trash))