from sys import stdin

N, M = map(int, stdin.readline().split())
floor = []
cnt = 0
visited = [[False for _ in range(M)] for __ in range(N)]

def dfs(ii, jj): 
  if(floor[ii][jj] == '|' and ii+1 < N and floor[ii+1][jj] == '|'):
    visited[ii+1][jj] = True
    dfs(ii+1, jj)
  elif(floor[ii][jj] == '-' and jj+1 < M and floor[ii][jj+1] == '-'):
    visited[ii][jj+1] = True
    dfs(ii, jj+1)
    

for _ in range(N):
  floor.append(stdin.readline().rstrip())

for i in range(N):
  for j in range(M):
    if(not visited[i][j]):
      visited[i][j] = True
      cnt += 1
      dfs(i, j)
      
print(cnt)