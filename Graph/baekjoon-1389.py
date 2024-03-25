from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())

link = [[] for _ in range(N+1)]
minCnt = 99999999
res = 0

# 입력받기
for _ in range(M):
  A, B = map(int, stdin.readline().split())
  link[A].append(B)
  link[B].append(A)
  
# 케빈 베이컨 총합 계산
def countKevin():
  global visited
  global q
  cnt = 0
  
  while(q):
    user, dis = q.popleft()
    visited[user] = True

    for friend in link[user]:
      if(not visited[friend]):
        cnt += dis
        visited[friend] = True
        q.append((friend, dis+1)) # depth 1 증가할 때 -> distance 1씩 증가
  return cnt

# 1 ~ N번 유저까지 각 케빈 베이컨 수 계산
for i in range(1, N+1):
  q = deque()
  q.append((i, 1)) # ( 현재 유저 번호, distance )
  visited = [False for _ in range(N+1)]
  
  iCnt = countKevin()
  if(minCnt > iCnt): # 최소 값 저장
    minCnt = iCnt
    res = i
    
print(res)