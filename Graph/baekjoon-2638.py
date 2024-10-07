# N * M 격자 / 치즈 1, 공기 0
# 4면 중 2면이 공기와 접촉 -> 1시간 뒤에 녹아 사라짐
# 치즈 내부 공간은 외부와 접촉하지 않는다고 가정
# 치즈가 모두 녹아 없어지는 시간 구하기

# 치즈가 아닌 공기를 타고 BFS 돌기
# 공기와 맞닿은 곳에 치즈가 있는지 확인 -> 스택 2번 쌓이면 1시간 뒤에 녹이기

from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
field = []
total = 0
cnt = 0
direct = [[0, 1], [0, -1], [1, 0], [-1, 0]]

for _ in range(n):
  inputList = list(map(int, stdin.readline().split()))
  field.append(inputList)
  total += inputList.count(1)

def meltCheese(meltList):
  for (i, j) in meltList:
    field[i][j] = 0
  return

def findMeltCheese():
  visited = [[False] * m for _ in range(n)]
  air = [[0] * m for _ in range(n)]
  melt = []
  q = deque()
  q.append((0, 0))
  
  # 항상 (0, 0)은 공기
  while(q):
    curI, curJ = q.popleft()
    for di, dj in direct:
      ii, jj = curI + di, curJ + dj
      if 0 <= ii < n and 0 <= jj < m:
        if not field[ii][jj] and not visited[ii][jj]:
          q.append((ii, jj))
          visited[ii][jj] = True
        elif field[ii][jj] == 1:
          air[ii][jj] += 1
    
  for i in range(n):
    for j in range(m):
      if air[i][j] >= 2:
        melt.append((i, j))
  
  return melt
  
# 모든 치즈가 녹을 때까지 반복
while(total != 0):
  melt = findMeltCheese()
  meltCheese(melt)
  total -= len(melt)
  cnt += 1
  
print(cnt)