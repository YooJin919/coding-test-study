from sys import stdin
from collections import deque

# 입력 받기
N = int(stdin.readline().rstrip())
graph = []
result = [["0" for _ in range(N)] for __ in range(N)]
for _ in range(N):
  graph.append(list(map(int, stdin.readline().split())))
  

def dfs(start, end, cur):
  global visited
  global stack
  
  for idx in range(N):
    if(not visited[idx] and graph[cur][idx]):
      visited[idx] = True
      stack.append(idx)
      if(idx == end):
        result[start][end] = str(1)
        return
      dfs(start, end, idx)
  stack.popleft()
    
  
# 모든 정점에 대한 경로 찾기
for i in range(N):
  for j in range(N):
    stack = deque()
    visited = [False for _ in range(N)]
    stack.append(i)
    # visited[i] = True
    dfs(i, j, i)
  
# 결과 출력
for _ in range(N):
  print(' '.join(result[_]))