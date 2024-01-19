from sys import stdin

n = int(stdin.readline().rstrip())
res = [-1 for _ in range(1000001)]

res[2] = 1
res[4] = 2
res[5] = 1

for i in range(6, n+1):
  if(res[i-5] >= res[i-2]):
    if(res[i-2] != -1):
      res[i] = res[i-2] + 1
    elif(res[i-5] != -1):
      res[i] = res[i-5] + 1
    else:
      res[i] = -1
  else:
    if(res[i-5] != -1):
      res[i] = res[i-5] + 1
    elif(res[i-2] != -1):
      res[i] = res[i-2] + 1
    else:
      res[i] = -1
print(res[n])