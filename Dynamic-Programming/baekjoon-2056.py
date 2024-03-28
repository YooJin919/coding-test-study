from sys import stdin

N = int(stdin.readline().rstrip())
dp = [0] * (N+1)
task = [0] * (N+1)
time = [0] * (N+1)

for i in range(1, N+1):
    t, count, *preTask = map(int, input().split())
    task[i] = preTask
    dp[i] = t
    time[i] = t

for i in range(1, N+1):
  for t in task[i]:
    dp[i] = max(dp[i], dp[t]+time[i])

print(max(dp))