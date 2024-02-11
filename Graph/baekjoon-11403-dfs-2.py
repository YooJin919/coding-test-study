# (1)-2 DFS (노드 갯수만큼 반복) 104ms
from sys import stdin

# 입력 받기
N = int(stdin.readline().rstrip())
graph = []
for _ in range(N):
  graph.append(list(map(int, stdin.readline().split())))
  
def dfs(node): 
  global check 
  for i in range(N):
    if(check[i] == "0" and graph[node][i]):
      check[i] = "1"
      dfs(i)

for node in range(N):
  check = ["0" for _ in range(N)]
  dfs(node)
  print(' '.join(check))