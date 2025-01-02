# 지도 R X C
# X : 땅
# . : 바다
# 50년 후 인접한 3칸 or 4칸에 바다가 존재하는 땅은 잠김

# 50년 후 지도를 그리기
# 지도 크기 : 모든 섬을 포함하는 가장 작은 직사각형

from sys import stdin

d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
r, c = map(int, stdin.readline().split())
map = []
check = [[0 for _ in range(c)] for __ in range(r)]
x1, y1, x2, y2 = 9999, 9999, -9999, -9999

for _ in range(r):
  map.append(list(stdin.readline().rstrip()))

for i in range(r):
  for j in range(c):
    if map[i][j] == '.':
      for [dx, dy] in d:
        ii = i + dx
        jj = j + dy
        if 0 <= ii < r and 0 <= jj < c and map[ii][jj] == 'X':
          check[ii][jj] += 1
    else:
      if i <= 0:
        check[i][j] += 1
      if i >= r-1:
        check[i][j] += 1
      if j <= 0:
        check[i][j] += 1
      if j >= c-1:
        check[i][j] += 1

for i in range(r):
  for j in range(c):
    if check[i][j] >= 3:
      map[i][j] = '.'
    if map[i][j] == 'X':
      x1 = i if (i < x1) else x1
      y1 = j if (j < y1) else y1
      x2 = i if (i > x2) else x2
      y2 = j if (j > y2) else y2

for i in range(x1, x2+1):
  for j in range(y1, y2+1):
    print(map[i][j], end="")
  print()