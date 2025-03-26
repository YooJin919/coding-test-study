# N X N
# 선생님 / 학생 / 장애물
# 선생님 : 상하좌우 감시 (장애물 뒤 학생 못 봄)
# 장애물 3개 설치 -> 모든 학생이 감시 피할 수 있도록

# 장애물 설치 가능한 모든 경우에서 감시를 피할 수 있는지 확인

from sys import stdin

N = int(stdin.readline().rstrip())
passage = []
teacherPos = []
isPossible = False

for i in range(N):
  arr = list(stdin.readline().split())
  passage.append(arr)
  
  for j in range(N):
    if arr[j] == 'T':
      teacherPos.append((i, j))
      
def checkTeacher():
  for (i, j) in teacherPos:
    # 상
    for k in range(i-1, -1, -1):
      if passage[k][j] == 'S':
        return False
      elif passage[k][j] == 'O':
        break
    
    # 하
    for k in range(i+1, N):
      if passage[k][j] == 'S':
        return False
      elif passage[k][j] == 'O':
        break
      
    # 좌
    for k in range(j-1, -1, -1):
      if passage[i][k] == 'S':
        return False
      elif passage[i][k] == 'O':
        break
    
    # 우
    for k in range(j+1, N):
      if passage[i][k] == 'S':
        return False
      elif passage[i][k] == 'O':
        break
  return True

# backtracking으로 가능한 모든 경우의 장애물 3개 설치
def placeObject(objectCnt):
  if objectCnt == 3:
    if checkTeacher():
      print("YES")
      exit()
    return
  
  for i in range(N):
    for j in range(N):
      if passage[i][j] == 'X':
        passage[i][j] = 'O'
        placeObject(objectCnt + 1)
        passage[i][j] = 'X'

placeObject(0)
  
print("NO")