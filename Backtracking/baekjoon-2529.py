from sys import stdin
from collections import deque

k = int(stdin.readline().rstrip())
sign = deque(stdin.readline().split())
used = [False for _ in range(10)]

minRes = "9999999999"
maxRes = "-9999999999"

def check(sign, before, cur):
  if(sign == '<'):
    return before < cur
  else:
    return before > cur

def dfs(depth, num):
  global minRes, maxRes
  if(depth == k+1):
    if(num < minRes):
      minRes = num
    elif(maxRes < num):
      maxRes = num
    return
  
  for i in range(10):
    if(not used[i]):
      if(depth == 0 or check(sign[depth-1], num[-1], str(i))):
        used[i] = True
        dfs(depth+1, num+str(i))
        used[i] = False


dfs(0, "")
print(maxRes)
print(minRes)