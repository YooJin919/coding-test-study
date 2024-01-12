from sys import stdin
from collections import deque

N, M, V = map(int, stdin.readline().rstrip().split(" "))
graph = [[0] * (N+1) for _ in range(N+1)]
visited = [False] * (N+1)
stack = deque()

# BFS
def BFS(v):
  q = deque()
  q.append(v)
  visited[v] = True
  
  while(q):
    top = q.popleft()
    print(top, end=" ")
    for idx in range(1, N+1):
      if(not visited[idx] and graph[top][idx]):
        q.append(idx)
        visited[idx] = True
        
# DFS
def DFS(v):
  print(v, end=" ")
  for idx in range(1, N+1):
    if(not visited[idx] and graph[v][idx]):
      stack.append(idx)
      visited[idx] = True  
      DFS(idx)
  stack.pop()

# Graph 입력받기
for _ in range(M):
  a, b = map(int, stdin.readline().rstrip().split(" "))
  graph[a][b] = 1
  graph[b][a] = 1
  
# DFS 호출
stack.append(V)
visited[V] = True
DFS(V)

# 방문여부 초기화
for idx in range(1, N+1):
  visited[idx] = False
print()

# BFS 호출
BFS(V)