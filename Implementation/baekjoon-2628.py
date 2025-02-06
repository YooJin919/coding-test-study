# 직사각형 종이, 가로 세로 1cm 점선
# 가로 점선 : 위에서 아래로 1 ~ N번, 세로 점선 : 왼쪽에서 오른쪽으로 1 ~ N번
# 칼로 종이 자르기 (왼 끝 -> 오른 끝 / 위 끝 -> 아래 끝)
# 종이를 점선을 따라 잘랐을 때 조각난 종이 중 가장 큰 종이의 넓이 출력

from sys import stdin
from collections import deque

c, r = map(int, stdin.readline().split())
cutCnt = int(stdin.readline().rstrip())
papers = deque()
papers.append([[0, 0], [r, c]])

for _ in range(cutCnt):
  direction, point = map(int, stdin.readline().split())
  l = len(papers)
  while(l):
    if direction == 0: # 가로 자르기
      [a, b] = papers.popleft()
      if a[0] < point < b[0]:
        papers.append([a, [point, b[1]]])
        papers.append([[point, a[1]], b])
      else:
        papers.append([a, b])
    elif direction == 1: # 세로 자르기
      [a, b] = papers.popleft()
      if a[1] < point < b[1]:
        papers.append([a, [b[0], point]])
        papers.append([[a[0], point], b])
      else:
        papers.append([a, b])
    l -= 1
        
size = []
for [a, b] in papers:
  size.append((b[0]-a[0]) * (b[1]-a[1]))
print(max(size))