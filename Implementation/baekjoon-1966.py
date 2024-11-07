from collections import deque
import sys

t = int(sys.stdin.readline().rstrip())

for i in range(t):
  cnt = 0
  idx = 0
  arr = deque()
  prio = deque()
  docNum, wantidx = map(int, sys.stdin.readline().split())
  inp = list(map(int, sys.stdin.readline().split()))
  
  for i in range(docNum):
    prio.append([idx, inp[i]])
    idx+=1

  while(len(prio)>0):
    m = max(prio, key=lambda x:x[1])
    if prio[0][1] == m[1]:
      if prio[0][0]==wantidx:
        cnt+=1
        print(cnt)
        break
      else:
        n = prio.popleft()
        cnt+=1
    else:
      prio.append(prio.popleft())