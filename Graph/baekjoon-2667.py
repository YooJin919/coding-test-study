# 정사각형 지도
# 집 있으면 O, 집 없으면 X
# 단지 번호 붙이기 (상, 하, 좌, 우 -> 같은 단지)
# 같은 단지에 속하는 집의 수를 오름차순으로 출력
# 단지가 3개, 각 7집, 8개, 9개 -> 3, 7, 8, 9

from sys import stdin
from collections import deque

n = int(stdin.readline().rstrip())
field = []
cntList = []
cnt = 0
visited = [[False] * n for _ in range(n)]
d = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def checkHouse(i, j):
  cnt = 0
  
  q = deque()
  q.append((i, j))
  visited[i][j] = True
  
  while(q):
    curI, curJ = q.popleft()
    cnt += 1
    for [di, dj] in d:
      nowI = curI + di
      nowJ = curJ + dj
      
      if 0 <= nowI < n and 0 <= nowJ < n:
        if not visited[nowI][nowJ] and field[nowI][nowJ]:
          q.append((nowI, nowJ))
          visited[nowI][nowJ] = True
        
  return cnt
  
for _ in range(n):
  field.append(list(map(int, stdin.readline().rstrip())))
  
for i in range(n):
  for j in range(n):
    if field[i][j] and not visited[i][j]:
      cnt += 1
      cntList.append(checkHouse(i, j))
  
print(cnt)
cntList.sort()
for c in cntList:
  print(c)