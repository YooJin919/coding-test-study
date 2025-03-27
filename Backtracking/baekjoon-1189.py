# 왼쪽 아래 시작
# 오른쪽 위 도착
# 지나간 곳은 다시 방문 불가
# 집으로 가는 다양한 길 중 거리 K인 경우의 수 출력

# dfs로 갈 수 있는 모든 거리 확인, depth = K 체크

from sys import stdin

r, c, k = map(int, stdin.readline().split())
visited = [[False] * c for _ in range(r)]
d = [[0, 1], [1, 0], [-1, 0], [0, -1]]
road = []
cnt = 0

for _ in range(r):
  road.append(list(stdin.readline().rstrip()))

def findRoute(point, depth):
  global cnt
  (nowR, nowC) = point
  
  if nowR == 0 and nowC == c-1:
    if depth == k:
      cnt += 1
    return
  
  for [dr, dc] in d:
    curR = nowR + dr
    curC = nowC + dc
    
    if 0 <= curR < r and 0 <= curC < c and not visited[curR][curC] and road[curR][curC] == '.':
      visited[curR][curC] = True
      findRoute((curR, curC), depth+1)
      visited[curR][curC] = False

visited[r-1][0] = True
findRoute((r-1, 0), 1)
print(cnt)