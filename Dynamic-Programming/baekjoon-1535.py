# 생각해준 사람 N명 (1~N번)
# i번 사람에게 인사, L[i] 체력 소모, J[i] 기쁨 획득
# 1사람 당 1번 감사인사 가능
# 주어진 체력에서 최대의 기쁨을 얻기. 체력 = 100, 기쁨 = 0
# 최대 기쁨 반환

from sys import stdin

N = int(stdin.readline().rstrip())
L = [0] + list(map(int, stdin.readline().split()))
J = [0] + list(map(int, stdin.readline().split()))
dp = [[0]*101 for _ in range(N+1)]

for i in range(1, N+1):
  for j in range(1, 101):
    if L[i] <= j: # 주어진 체력보다 소모량이 적은 경우
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-L[i]]+J[i])
    else:
      dp[i][j] = dp[i-1][j]

print(dp[N][99])

