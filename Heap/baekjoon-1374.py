from sys import stdin
import heapq

N = int(stdin.readline().rstrip())
lecture = []
room = [] # 강의 종료 시간 저장 (최소 힙 - pop하면 제일 빨리 종료되는 강의 나옴)
res = 0

for _ in range(N):
  num, start, end = map(int, stdin.readline().split())
  lecture.append([start, end])
  
lecture.sort(key= lambda x: x[0])
    
for l in lecture:
  while(room):
    if(room[0] <= l[0]):
      heapq.heappop(room)
    else:
      break
  heapq.heappush(room, l[1])
  res = max(len(room), res)
  
print(res)