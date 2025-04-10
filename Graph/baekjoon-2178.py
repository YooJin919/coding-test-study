# 1 이동 가능 / 0 이동 불가능
# (1, 1) 출발 (N, M) 도착
# 이동 거리 최소 칸 수 출력 (출발, 도착도 포함)

from sys import stdin
from collections import deque

maze = []
d = [[0, 1], [0, -1], [1, 0], [-1, 0]]

n, m = map(int, stdin.readline().split())

for _ in range(n):
  maze.append(list(map(int, ''.join(stdin.readline().split()))))

visited = [[False] * m for _ in range(n)]
distance = [[m * n] * m for _ in range(n)]
distance[0][0] = 1

def bfs():
  global distance
  q = deque()
  q.append((0, 0)) # x, y
  
  while(q):
    nowX, nowY = q.popleft()
    for di in d:
      curX = nowX + di[0]
      curY = nowY + di[1]
      
      if 0 <= curX < n and 0 <= curY < m:
        if maze[curX][curY] == 1 and not visited[curX][curY]:
          distance[curX][curY] = distance[nowX][nowY] + 1
          q.append((curX, curY))
          visited[curX][curY] = True
    
bfs()
print(distance[n-1][m-1])