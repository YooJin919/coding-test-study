## 인접행렬 + DFS ###
from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().rstrip().split(" "))
graph = [[0] * (N+1) for _ in range(N+1)]
for _ in range(N-1):
  a, b, dis = map(int, stdin.readline().rstrip().split(" "))
  graph[a][b] = dis
  graph[b][a] = dis
  
def DFS(cur, target, dis):
  if(cur == target):
    print(dis)
  for idx in range(1, N+1):
    if(not visited[idx] and graph[cur][idx]):
      stack.append(idx)
      visited[idx] = True
      DFS(idx, target, dis + graph[cur][idx])
  stack.pop()
  
for _ in range(M):
  visited = [False] * (N+1)
  stack = deque()
  a, b = map(int, stdin.readline().rstrip().split(" "))
  stack.append(a)
  visited[a] = True
  DFS(a, b, 0)
  
## 인접행렬 + BFS ###
from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().rstrip().split(" "))
graph = [[0] * (N+1) for _ in range(N+1)]
for _ in range(N-1):
  a, b, dis = map(int, stdin.readline().rstrip().split(" "))
  graph[a][b] = dis
  graph[b][a] = dis
  
def BFS(target):
  while(q):
    v = q.popleft()
    if(v[0] == target):
      print(v[1])
      return
    for idx in range(1, N+1):
      if(not visited[idx] and graph[v[0]][idx]):
        q.append((idx, v[1]+graph[v[0]][idx]))
        visited[idx] = True
  
for _ in range(M):
  visited = [False] * (N+1)
  a, b = map(int, stdin.readline().rstrip().split(" "))
  q = deque()
  q.append((a, 0))
  BFS(b)