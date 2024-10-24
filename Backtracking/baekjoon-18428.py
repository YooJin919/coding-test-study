from sys import stdin

n = int(stdin.readline().rstrip())
school = []
teacherList = []

# 입력 받기
for _ in range(n):
  school.append(stdin.readline().split())

def checkBlock():
  for (tx, ty) in teacherList:
    for i in range(tx - 1, -1, -1):
      if school[i][ty] == 'O':
        break
      elif school[i][ty] == 'S':
        return False
    for j in range(ty - 1, -1, -1):
      if school[tx][j] == 'O':
        break
      elif school[tx][j] == 'S':
        return False
    for i in range(tx + 1, n):
      if school[i][ty] == 'O':
        break
      elif school[i][ty] == 'S':
        return False
    for j in range(ty + 1, n):
      if school[tx][j] == 'O':
        break
      elif school[tx][j] == 'S':
        return False
  return True


def dfs(cnt):
  if cnt == 3:
    if checkBlock():
      print("YES")
      exit()
    return
  for i in range(n):
    for j in range(n):
      if school[i][j] == 'X':
        school[i][j] = 'O'
        dfs(cnt + 1)
        school[i][j] = 'X'

# 선생님 좌표 저장
for i in range(n):
  for j in range(n):
    if school[i][j] == 'T':
      teacherList.append((i, j))

dfs(0)
print("NO")