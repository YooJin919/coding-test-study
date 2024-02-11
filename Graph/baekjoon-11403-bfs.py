# (2) BFS 96ms
from sys import stdin
from collections import deque

# 입력 받기
N = int(stdin.readline().rstrip())
matrix = []
result = [["0" for _ in range(N)] for __ in range(N)]
for _ in range(N):
  matrix.append(list(map(int, stdin.readline().split())))
  
  
def bfs(node):
  q = deque()
  q.append(node)
  visited = [False for _ in range(N)]
  
  while(q):
    cur = q.popleft()
    for i in range(N):
      if(visited[i] == False and matrix[cur][i]):
        q.append(i)
        visited[i] = True
        result[node][i] = "1"

for n in range(N):
  bfs(n)
  
for _ in result:
  print(' '.join(_))