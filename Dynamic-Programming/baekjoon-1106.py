# 호텔 수입 늘리기
# 홍보 비용, 늘어나는 호텔 고객 수 (고정)
# **적어도** C명의 고객을 늘리기 위해 투자해야 하는 돈의 최솟값 출력

from sys import stdin

c, n = map(int, stdin.readline().split())
costPerCustomerNum = []
dp = [999999 for _ in range(c+100)] # dp[확보한 고객 수] = 최소 비용
dp[0] = 0

for _ in range(n):
  cost, num = map(int, stdin.readline().split())
  costPerCustomerNum.append([cost, num])

for i in range(1, c+100):
  for cost, customerNum in costPerCustomerNum:
    dp[i] = min(dp[i-customerNum] + cost, dp[i])
    
print(min(dp[c:]))