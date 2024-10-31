# F : 한 눈금 앞으로 [0, 1] -> d * (+1)
# B : 한 눈금 뒤로 [0, -1] -> d * (-1)
# L : 왼쪽으로 90도 회전 -> d[i-1]
# R : 오른쪽으로 90도 회전 -> d[i+1]

from sys import stdin

# 0: 상, 1: 우, 2:하, 4: 좌
d = {0: [-1, 0], 1: [0, 1], 2: [1, 0], 3: [0, -1]}

T = int(stdin.readline().rstrip())

def checkPoint(curD, p):
  global left, right, top, bottom
  
  if curD == 0 or curD == 2:
    if top > p[0]:
      top = p[0]
    if bottom < p[0]:
      bottom = p[0]
      
  if curD == 1  or curD == 3:
    if right < p[1]:
      right = p[1]
    if left > p[1]:
      left = p[1]
  return

for _ in range(T):
  control = list(stdin.readline().rstrip())
  left, right, top, bottom = 0, 0, 0, 0
  cur = [0, 0]
  curD = 0
  for c in control:
    if c == "F":
      cur = [cur[0]+d[curD][0], cur[1]+d[curD][1]]
    elif c == "B":
      cur = [cur[0]-d[curD][0], cur[1]-d[curD][1]]
    elif c == "L":
      curD -= 1
      if curD < 0:
        curD = 3
    elif c == "R":
      curD += 1
      if curD > 3:
        curD = 0
    checkPoint(curD, cur)
  print((right - left) * (bottom - top))