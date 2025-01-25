# 중요도가 높은 N개 일부터 한다.
# 하루에 하나의 일만 처리
# 일을 처리한 후 중요도(M)만큼 감소
# 완료된 일: 일의 중요도 <= K

# 오늘의 만족감(내림) = 전날의 만족감(Y)/2 + 오늘 할 일의 중요도(P)

# 일을 다 하기 위해 걸리는 날 출력
# 일별 만족도 출력

from sys import stdin
import heapq

n, m, k = map(int, stdin.readline().split())
k = -k
d = []
satisfaction = [0]

for _ in range(n):
  heapq.heappush(d, -int(stdin.readline().rstrip()))

while(d):
  mostM = heapq.heappop(d)
  satisfaction.append(satisfaction[-1]//2 + (-mostM))
  mostM += m
  if mostM < k:
    heapq.heappush(d, mostM)
    
print(len(satisfaction)-1)
for s in satisfaction[1:]:
  print(s)