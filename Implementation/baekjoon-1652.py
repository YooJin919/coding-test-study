from sys import stdin

N = int(stdin.readline().rstrip())

room = []
cntR = 0
cntC = 0

for _ in range(N):
  room.append(stdin.readline().rstrip())

# 가로
for i in range(N):
  emptyNum = 0
  for j in range(N):
    if(room[i][j] == "."):
      emptyNum += 1
      if(j+1 < N and room[i][j+1] == "."):
        continue
      elif(j+1 >= N or room[i][j+1] == "X"):
        if(emptyNum >= 2):
          cntR += 1
        emptyNum = 0
      
# 세로
for j in range(N):
  emptyNum = 0
  for i in range(N):
    if(room[i][j] == "."):
      emptyNum += 1
      if(i+1 < N and room[i+1][j] == "."):
        continue
      elif(i+1 >= N or room[i+1][j] == "X"):
        if(emptyNum >= 2):
          cntC += 1
        emptyNum = 0
    
print(cntR, cntC)