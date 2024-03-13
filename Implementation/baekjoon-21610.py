from sys import stdin

N, M = map(int, stdin.readline().split())
basket = []
d = {1:[0, -1], 2:[-1, -1], 3:[-1, 0], 4:[-1, 1], 5:[0, 1], 6:[1, 1], 7:[1, 0], 8:[1, -1]}

for _ in range(N):
  basket.append(list(map(int, stdin.readline().split())))
disi = []
for _ in range(M):
  disi.append(tuple(map(int, stdin.readline().split())))

cloud = [(N-1, 0), (N-2, 0), (N-1, 1), (N-2, 1)] # 현재 구름 위치 (r, c)
cloud = set(cloud)
  
for di, si in disi:  
  # 1) di 방향으로 si 만큼 구름 이동
  movedCloud = set()
  for r, c in cloud:
    newR = (r + (d[di][0] * si)) % N
    newC = (c + (d[di][1] * si)) % N
    movedCloud.add((newR, newC))
    basket[newR][newC] += 1 # 2) 이동한 구름 칸 물 + 1
    
  # 4) 이동한 구름 칸에 물 복사 버그 마법 사용
  for r, c in movedCloud:
    cnt = 0 # 대각선 4방에 물 존재하는 바구니 수
    for i in [2, 4, 6, 8]:
      newR = (r + d[i][0])
      newC = (c + d[i][1])
      if(0 <= newR < N and 0 <= newC < N and basket[newR][newC] > 0):
          cnt += 1
    basket[r][c] += cnt
  
  # 5) 물 양 >= 2 칸 구름 생성 ** 이동한 구름 칸 제외 **
  newCloud = set()
  for i in range(N):
    for j in range(N):
      if(basket[i][j] >= 2 and ((i, j) not in movedCloud)):
        newCloud.add((i, j))
        basket[i][j] -= 2
  
  cloud = newCloud

# 바구니에 들어있는 물의 합
res = 0
for b in basket:
  res += sum(b)

print(res)