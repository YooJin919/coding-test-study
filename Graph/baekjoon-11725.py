# 루트 없는 트리
# 트리의 루트 = 1
# 각 노드의 부모 구하기

from sys import stdin
from collections import deque

num = int(stdin.readline().rstrip())
tree = [[] for _ in range(num + 1)]
res = [0 for _ in range(num + 1)]

for _ in range(num - 1):
  n, m = map(int, stdin.readline().split())
  tree[n].append(m)
  tree[m].append(n)

q = deque()
q.append(1)
res[1] = 1

while(q):
   cur = q.popleft()
   nodeList = tree[cur]
   
   for n in nodeList:
     if res[n] == 0:
       res[n] = cur
       q.append(n)
       
for i in range(2, num + 1):
  print(res[i])