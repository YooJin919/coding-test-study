from sys import stdin
from collections import deque

N = int(stdin.readline().rstrip())
human = deque(map(int, stdin.readline().split()))
res = deque()

for i in range(N-1, -1, -1):
  res.insert(human[i], str(i+1))

print(' '.join(res))

