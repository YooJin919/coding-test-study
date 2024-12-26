# 상근이 동기 중 친구, 친구의 친구 초대
# 동기 N명 (학번 : 1 ~ N번), 상근이 : 1번
# 친구 관계 조사 리스트 -> 결혼식에 초대할 사람의 수 구하기

from sys import stdin
from collections import deque

n = int(stdin.readline().rstrip())
num = int(stdin.readline().rstrip())
relation = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(num):
  a, b = map(int, stdin.readline().split())
  relation[a].append(b)
  relation[b].append(a)
  
def findFriends():
  global visited, relation
  cnt = 0
  q = deque()
  q.append((1, 0))
  visited[1] = True
  
  while(q):
    cur, depth = q.popleft()
    for cmp in relation[cur]:
      if not visited[cmp] and depth < 2:
        visited[cmp] = True
        q.append((cmp, depth+1))
        cnt += 1
  
  return cnt

print(findFriends())