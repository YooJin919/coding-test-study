from sys import stdin

houseNum = int(stdin.readline().rstrip())
cost = [list(map(int, stdin.readline().split())) for __ in range(houseNum)]

for i in range(1, houseNum):
  cost[i][0] += min(cost[i-1][1], cost[i-1][2])
  cost[i][1] += min(cost[i-1][0], cost[i-1][2])
  cost[i][2] += min(cost[i-1][0], cost[i-1][1])

print(min(cost[houseNum-1]))