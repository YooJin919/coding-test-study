from sys import stdin

N, M = map(int, stdin.readline().split())
r, c, d = map(int, stdin.readline().split())
room = []
cnt = 0

for _ in range(N):
  room.append(list(map(int, stdin.readline().split())))
  
def cleanRoom(curR, curC, curD, cnt):
  di = {0:[-1, 0], 1:[0, 1], 2:[1, 0], 3:[0, -1]}
  if(room[curR][curC] == 0): # 현재 칸 빈칸이면 청소
    room[curR][curC] = 999
    cnt += 1
    
  # 빈칸 확인
  for i in range(4):
    if(room[curR+di[i][0]][curC+di[i][1]] == 0): # 주변 4칸 중 빈칸 존재
      for _ in range(4):
        curD -= 1 # 반시계 회전
        if(curD < 0):
          curD = 3
        if(room[curR+di[curD][0]][curC+di[curD][1]] == 0): # 반시계 회전한 상태로 전진
          break
      cleanRoom(curR+di[curD][0], curC+di[curD][1], curD, cnt)
      return
  # 빈칸 없음
  for j in range(4): # 후진 방향 찾기
    if(abs(curD-j)==2): 
      newD = j
      if(room[curR+di[newD][0]][curC+di[newD][1]] != 1): #후진 가능한가
        cleanRoom(curR+di[newD][0], curC+di[newD][1], curD, cnt)
        return
      elif(room[curR+di[newD][0]][curC+di[newD][1]] == 1): # 바라보는 방향에서 1칸 후진 시 벽 == STOP
        print(cnt)
        return
        
  
cleanRoom(r, c, d, cnt)