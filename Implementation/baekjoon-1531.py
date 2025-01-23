# 100 X 100 그림 (1, 1) ~ (100, 100)
# N개의 불투명 종이로 그림 가리기
# 그림의 현재 부분 위에 M개 이하의 종이가 올려져 있으면 그림은 그 부분에서 보임

# 보이지 않는 그림의 개수 반환

from sys import stdin

n, m = map(int, stdin.readline().split())
picture = [[0]*100 for _ in range(100)]
res = 0

for _ in range(n):
  ax, ay, bx, by = map(int, stdin.readline().split())
  
  for i in range(ax-1, bx):
    for j in range(ay-1, by):
      picture[i][j] += 1
  
for i in range(100):
  for j in range(100):
    if picture[i][j] > m:
      res += 1
      
print(res)