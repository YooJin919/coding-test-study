# 1 ~ N^2로 채워진 N X N 배열 (N = 3 고정)
# 매직 스퀘어 : 모든 행, 열, 길이가 N인 대각선의 합이 모두 같음

# a를 b로 변경하는 비용 = |a-b|
# 주어진 배열을 매직 스퀘어로 변경하는 비용의 최솟값 반환

# 1. 3X3 배열에 임의의 숫자 다 넣기
# 2. 9개가 채워지면 매직 스퀘어인지 확인
# 3-1. 매직 스퀘어라면 비용 계산하고 최솟값이랑 비교
# 3-2. 매직 스퀘어가 아니라면 값 1개 변경하고 다시 2번으로 돌아감 (dfs, backtracking)

from sys import stdin

arr = []
for _ in range(3):
  arr.append(list(map(int, stdin.readline().split())))

res = 9999999
cmpList = [[0] * 3 for _ in range(3)]
visited = [False] * 10

def calculateCost():
  global res
  cost = 0
  for i in range(3):
    for j in range(3):
      cost += abs(arr[i][j] - cmpList[i][j])
  if cost < res:
    res = cost

def checkMagicSquare():
  global cmpList
  magic = 15

  # 행 확인
  for i in range(3):
    cmp = 0
    for j in range(3):
      cmp += cmpList[i][j]
    if cmp != magic:
      return False
  
  # 열 확인
  for i in range(3):
    cmp = 0
    for j in range(3):
      cmp += cmpList[j][i]
    if cmp != magic:
      return False

  # 대각선 확인
  cmp = 0
  cmp2 = 0
  for i in range(3):
    cmp += cmpList[i][i]
    cmp2 += cmpList[i][2-i]
  if cmp != magic or cmp2 != magic:
    return False
  
  return True

def dfs(cnt):
  global cmpList, visited
  if cnt == 9:
    if checkMagicSquare():
      calculateCost()
    return
  
  for i in range(1, 10):
    if visited[i]:
      continue
    visited[i] = True
    cmpList[cnt//3][cnt%3] = i
    dfs(cnt + 1)
    visited[i] = False

dfs(0)
print(res)