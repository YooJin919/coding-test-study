from sys import stdin

H, W = map(int, stdin.readline().split())
block = list(map(int, stdin.readline().split()))
world = [[False for _ in range(W)] for __ in range(H)]
cnt = 0

for i in range(W):
  idx = -1
  for idx in range(block[i]):
    world[idx][i] = True
    idx -= 1
    
for i in range(H):
  for j in range(1, W-1):
    if(world[i][j]):
      continue
    if(world[i][:j].count(True) and world[i][j:].count(True)):
      cnt += 1
      
print(cnt)