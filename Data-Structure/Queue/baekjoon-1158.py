import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

arr = deque(str(_) for _ in range(1, N+1))
res = []

while(arr):
  for _ in range(K-1):
    man = arr.popleft()
    arr.append(man)
  res.append(arr.popleft())

print("<"+", ".join(res)+">")