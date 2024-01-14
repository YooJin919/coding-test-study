import sys
sys.setrecursionlimit(100000)

totalNum = int(sys.stdin.readline().rstrip())
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def dfs(y, x):
  grid[y][x] = '.' # visited 배열 대신 grid에 직접 표시
  for d in range(4): # 상하좌우 양 있는지 탐색
    yy = y + dy[d]
    xx = x + dx[d]
    if(yy >= 0 and xx >= 0 and yy < n and xx < m):
      if(grid[yy][xx] == '#'):
        dfs(yy, xx)

for _ in range(totalNum):
  grid = []
  cnt = 0
  n, m = map(int, sys.stdin.readline().split(" "))
  
  # 양 위치 입력받기
  for __ in range(n):
    grid.append(list(sys.stdin.readline().rstrip()))
  
  # 양 무리 개수 
  for i in range(n):
    for j in range(m):
      if(grid[i][j] == '#'):
        dfs(i, j)
        cnt += 1
  
  print(cnt)
  