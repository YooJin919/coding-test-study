### 인접리스트 + DFS ###
from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().rstrip().split(" "))
graph = [[]*(N+1) for _ in range(N+1)]
for _ in range(N-1):
  a, b, dis = map(int, stdin.readline().rstrip().split(" "))
  graph[a].append((b, dis))
  graph[b].append((a, dis))
  
def DFS(curNode, target, curDis):
  if(curNode == target):
    print(curDis)
  for v, dis in graph[curNode]:
    if(not visited[v]):
      stack.append(v)
      visited[v] = True
      DFS(v, target, curDis + dis)
  stack.pop()
  
for _ in range(M):
  visited = [False] * (N+1)
  stack = deque()
  a, b = map(int, stdin.readline().rstrip().split(" "))
  stack.append(a)
  visited[a] = True
  DFS(a, b, 0)
  
### 인접리스트 + BFS ###
from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().rstrip().split(" "))
graph = [[]*(N+1) for _ in range(N+1)]
for _ in range(N-1):
  a, b, dis = map(int, stdin.readline().rstrip().split(" "))
  graph[a].append((b, dis))
  graph[b].append((a, dis))
  
def BFS(start, target, curDis):
  q = deque([(start, curDis)])
  visited[start] = True
  while(q):
    curNode, curDis = q.popleft()
    if(curNode == target):
      print(curDis)
      return
    for v, dis in graph[curNode]:
      if(not visited[v]):
        q.append((v, curDis + dis))
        visited[curNode] = True
  
for _ in range(M):
  visited = [False] * (N+1)
  a, b = map(int, stdin.readline().rstrip().split(" "))
  BFS(a, b, 0)