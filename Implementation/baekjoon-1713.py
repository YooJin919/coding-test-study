# 추천받은 학생의 사진을 게시하고 추천 횟수를 표시
# 1. 추천하면 반드시 사진이 게시
# 2. 비어있는 사진 틀 없으면 추천 횟수 가장 적은 학생 삭제 & 그 자리에 새로운 학생 게시
# 3. 최소 추천 개수가 동일한 학생이 여러 명이면 오래된 사진을 삭제
# 4. 존재하는 학생을 추천하면 횟수 증가
# 5. 사진 삭제되면 추천 0으로 리셋

# 최종 후보가 누구인지 오름차순 반환

from sys import stdin

frameCnt = int(stdin.readline().rstrip())
recommendCnt = int(stdin.readline().rstrip())
recommendedStudent = list(map(int, stdin.readline().split()))

frame = []

def findMinIndex():
  global frame
  minValue = 99999
  minIdx = 0
  for i in range(len(frame)):
    value = frame[i][0]
    if value < minValue:
      minValue = value
      minIdx = i
  return minIdx

def checkExistAndIncrease(studentNum):
  global frame
  for i in range(len(frame)):
    if frame[i][1] == studentNum:
      frame[i][0] += 1
      return True
  return False

for studentNum in recommendedStudent:
  if len(frame) == 0:
    frame.append([1, studentNum])
    continue
  if (not checkExistAndIncrease(studentNum)):
    if len(frame) == frameCnt:
      idx = findMinIndex()
      frame.pop(idx)
    frame.append([1, studentNum])
    
frame = sorted(list(frame), key=lambda x:x[1])
for student in frame:
  print(student[1], end=" ")
  