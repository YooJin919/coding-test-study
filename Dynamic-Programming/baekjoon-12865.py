# 물건 N개 (무게 W, 가치 V)
# 배낭에 넣을 수 있는 최대 무게 K
# 배낭에 넣을 수 있는 물건의 최대 가치 출력

from sys import stdin

n, k = map(int, stdin.readline().split())
items = [[0]]

# items[idx] = [무게, 가치]
for _ in range(n):
  items.append(list(map(int, stdin.readline().split())))

# valueList[물건 순서번호][총 무게] = 최대 가치
valueList = [[0] * (k+1) for _ in range(n+1)]

for idx in range(1, n+1):
  for stdWeight in range(1, k+1):
    if stdWeight >= items[idx][0]: # 무게 허용 범위
      valueList[idx][stdWeight] = max(valueList[idx-1][stdWeight], valueList[idx-1][stdWeight-items[idx][0]]+items[idx][1])
    else:
      valueList[idx][stdWeight] = valueList[idx-1][stdWeight]
      
print(valueList[n][k])
      