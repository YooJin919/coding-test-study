# N개 정수 순열 (1~N)
# 순열을 방향 그래프로 나타내고 -> 사이클을 파악 (순열 사이클)
# 수열 사이클 개수 반환

from sys import stdin

t = int(stdin.readline().rstrip())

def checkCycle(idx):
  global visited, arr
  visited[idx] = True
  
  if not visited[arr[idx-1]]:
    checkCycle(arr[idx-1])
  return

for _ in range(t):
  res = 0
  n = int(stdin.readline().rstrip())
  arr = list(map(int, stdin.readline().split()))
  visited = [False for __ in range(n+1)]

  for idx in range(1, n+1):
    if not visited[idx]:
      checkCycle(idx)
      res += 1
      
  print(res)