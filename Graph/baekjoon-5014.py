from sys import stdin
from collections import deque

F, S, G, U, D = map(int, stdin.readline().split())
visited = [False for _ in range(F+1)]
cnt = [0 for _ in range(F+1)]
q = deque()

def bfs(start):
  q.append(start)
  visited[start] = True
  while(q):
    cur = q.popleft()
    if(cur == G):
      print(cnt[G])
      return
    for i in (cur+U, cur-D):
      if(i > 0 and i <= F and not visited[i]):
        cnt[i] = cnt[cur] + 1
        visited[i] = True
        q.append(i)
  if(cnt[G] == 0):
    print("use the stairs")
        
bfs(S)