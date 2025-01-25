# 1초가 지날 때마다 1개씩 새로운 꽃이 피어남
# 꽃 좌표 (x0, y0), t초 후에 피어난 꽃 좌표 (xt, yt) -> x(t+1) + y(t+1)

# xt+1 + yt+1 < R -> x(t+1) = xt+1, y(t+1) = yt+1
# xt+1 + yt+1 >= R -> x(t+1) = xt/2, y(t+1) = yt/2

# 모든 값은 정수, 여러 송이가 한 좌표에 필 수 있음

# 비어있는 정원 (a, b)에 꽃이 필 때, 한 좌표에 2개 꽃이 피는 최소 시간 반환

from sys import stdin

a, b = map(int, stdin.readline().split())
r = int(stdin.readline().rstrip())
time = 0
garden = {(a, b): 1}

while(1):
  time += 1
  if a + b + 2 < r:
    a = a + 1
    b = b + 1
  else:
    a = a // 2
    b = b // 2
  if (a, b) in garden:
    break
  else:
    garden[(a, b)] = 1

print(time)